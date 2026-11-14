// Run: node scripts/fetch-snapshots.mjs  -> refreshes data/spaceweather.json (no API key needed)
import { writeFile } from 'node:fs/promises';
const N='https://services.swpc.noaa.gov';
const j=async u=>(await fetch(N+u,{signal:AbortSignal.timeout(15000)})).json();
const o={fetchedAt:new Date().toISOString(),pfu:null,kp:null,flux:null,wind:null};
try{const p=(await j('/json/goes/primary/integral-protons-6-hour.json')).filter(q=>q.energy==='>=10 MeV').pop();if(p){o.pfu=+p.flux;o.fetchedAt=new Date(p.time_tag).toISOString()}}catch{}
try{const k=(await j('/json/planetary_k_index_1m.json')).pop(),v=Array.isArray(k)?k[1]:(k.estimated_kp??k.kp_index??k.kp);if(!isNaN(+v))o.kp=+v}catch{}
try{const x=(await j('/json/goes/primary/xrays-6-hour.json')).filter(q=>String(q.energy).startsWith('0.1-0.8')).pop();if(x)o.flux=+x.flux}catch{}
try{const w=(await j('/products/solar-wind/plasma-2-hour.json')).pop();if(w&&!isNaN(+w[2]))o.wind=+w[2]}catch{}
if(o.pfu!==null||o.kp!==null){await writeFile('data/spaceweather.json',JSON.stringify(o));console.log('saved',o)}else console.log('no data, kept old file');
