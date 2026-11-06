import subprocess, json, sys
from pathlib import Path

pairs=json.loads(sys.argv[1])
script=r'''async (page) => {
for(const [id,row,state] of PAIRS){
 await page.getByRole('combobox',{name:'角色版本',exact:true}).selectOption(id);
 await page.getByRole('combobox',{name:'动作',exact:true}).selectOption(String(row));
 await page.waitForFunction(()=>!document.getElementById('note').textContent.includes('正在载入'));

 await page.evaluate(async ({id,state}) => {
 document.getElementById('restart').click();
 const samples=[];let prev='',seenThird=false;
 await new Promise((resolve,reject)=>{const started=performance.now();function sample(){const pos=document.getElementById('position').textContent;if(pos!==prev){prev=pos;const c=document.createElement('canvas');c.width=192;c.height=208;c.getContext('2d').drawImage(document.getElementById('after'),0,0);samples.push({pos,c});if(pos.includes('第 3 轮'))seenThird=true;if(seenThird&&pos.startsWith('待机')){resolve();return}}if(performance.now()-started>8000){reject('no third cycle to idle');return}requestAnimationFrame(sample)}sample()});
 const old=document.getElementById('qa-grid');if(old)old.remove();const grid=document.createElement('canvas');grid.id='qa-grid';grid.width=1536;grid.height=Math.ceil(samples.length/8)*234+32;grid.style='display:block;width:1536px;height:'+grid.height+'px;max-width:none;background:#f4f1ed;margin:0';const ctx=grid.getContext('2d');ctx.fillStyle='#f4f1ed';ctx.fillRect(0,0,grid.width,grid.height);ctx.fillStyle='#222';ctx.font='14px sans-serif';ctx.fillText(id+' / '+state+' / Actual browser playback: 3 cycles then idle',8,20);samples.forEach((s,i)=>{const x=(i%8)*192,y=Math.floor(i/8)*234+32;ctx.fillText(s.pos,x+3,y+15);ctx.drawImage(s.c,x,y+24)});document.body.append(grid);
 }, {id,state});
 await page.locator('#qa-grid').screenshot({path:'output/playwright/final-motion-b/'+id+'--'+state+'--three-cycles.png'});
 await page.locator('#qa-grid').evaluate(el=>el.remove());
 await page.screenshot({path:'output/playwright/final-motion-b/'+id+'--'+state+'--idle-viewport.png'});
}
}'''.replace('PAIRS',json.dumps(pairs))
result=subprocess.run(['bash','/home/ubuntu23/.codex/skills/playwright/scripts/playwright_cli.sh','-s=final-motion-b','run-code',script],capture_output=True,text=True)
print(result.stdout);print(result.stderr)
