<?php
/**
 * Night Watch: Outpost Zero - Cloud Save Endpoint
 * Zero-login persistent storage for Porkbun / GoDaddy / PHP Web Hosting.
 */
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: GET, POST, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type");
header("Content-Type: application/json; charset=UTF-8");

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit;
}

$saveDir = __DIR__ . '/saves';
if (!is_dir($saveDir)) {
    @mkdir($saveDir, 0755, true);
    // Protect directory listing
    @file_put_contents($saveDir . '/index.html', '<!doctype html><title>Access Denied</title>');
}

// Generate new call sign
if (isset($_GET['new'])) {
    $prefixes = ['ARTEMIS', 'ORION', 'APOLLO', 'EAGLE', 'VOYAGER', 'GATEWAY', 'POLARIS', 'TITAN', 'NOVA'];
    $callsign = $prefixes[array_rand($prefixes)] . '-' . rand(100, 999);
    echo json_encode(['ok' => true, 'callsign' => $callsign]);
    exit;
}

// Load save
if ($_SERVER['REQUEST_METHOD'] === 'GET' && isset($_GET['id'])) {
    $id = strtoupper(preg_replace('/[^A-Za-z0-9_-]/', '', $_GET['id']));
    if (empty($id)) {
        http_response_code(400);
        echo json_encode(['ok' => false, 'error' => 'Invalid Call Sign']);
        exit;
    }
    $file = $saveDir . '/' . $id . '.json';
    if (!file_exists($file)) {
        http_response_code(404);
        echo json_encode(['ok' => false, 'error' => 'Mission not found on server']);
        exit;
    }
    $raw = @file_get_contents($file);
    $data = json_decode($raw, true);
    if (!$data) {
        http_response_code(500);
        echo json_encode(['ok' => false, 'error' => 'Corrupt save file']);
        exit;
    }
    echo json_encode(['ok' => true, 'callsign' => $id, 'save' => $data]);
    exit;
}

// Store save
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $input = file_get_contents('php://input');
    $payload = json_decode($input, true);
    if (!$payload || !isset($payload['callsign']) || !isset($payload['data'])) {
        http_response_code(400);
        echo json_encode(['ok' => false, 'error' => 'Missing callsign or data']);
        exit;
    }

    $id = strtoupper(preg_replace('/[^A-Za-z0-9_-]/', '', $payload['callsign']));
    if (strlen($id) < 3 || strlen($id) > 24) {
        http_response_code(400);
        echo json_encode(['ok' => false, 'error' => 'Call Sign must be 3-24 characters']);
        exit;
    }

    $file = $saveDir . '/' . $id . '.json';
    $toSave = [
        'v' => 2,
        'callsign' => $id,
        'updated_at' => date('c'),
        'S' => $payload['data']
    ];

    if (@file_put_contents($file, json_encode($toSave, JSON_PRETTY_PRINT)) === false) {
        http_response_code(500);
        echo json_encode(['ok' => false, 'error' => 'Failed to write save file on server']);
        exit;
    }

    echo json_encode(['ok' => true, 'callsign' => $id, 'saved_at' => $toSave['updated_at']]);
    exit;
}

echo json_encode(['ok' => true, 'service' => 'Night Watch Outpost Zero Cloud Save System', 'version' => '2.0']);
