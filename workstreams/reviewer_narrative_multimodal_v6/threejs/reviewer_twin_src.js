import {WebGLRenderer} from 'three/src/renderers/WebGLRenderer.js';
import {MeshStandardMaterial} from 'three/src/materials/MeshStandardMaterial.js';
import {SpriteMaterial} from 'three/src/materials/SpriteMaterial.js';
import {Mesh} from 'three/src/objects/Mesh.js';
import {Group} from 'three/src/objects/Group.js';
import {Sprite} from 'three/src/objects/Sprite.js';
import {BoxGeometry} from 'three/src/geometries/BoxGeometry.js';
import {SphereGeometry} from 'three/src/geometries/SphereGeometry.js';
import {CanvasTexture} from 'three/src/textures/CanvasTexture.js';
import {Scene} from 'three/src/scenes/Scene.js';
import {Color} from 'three/src/math/Color.js';
import {PerspectiveCamera} from 'three/src/cameras/PerspectiveCamera.js';
import {HemisphereLight} from 'three/src/lights/HemisphereLight.js';
import {DirectionalLight} from 'three/src/lights/DirectionalLight.js';
import {SRGBColorSpace} from 'three/src/constants.js';
import DATA from './reviewer-data.json';
const C={paper:0xf3f1e9,ink:0x26312d,red:0xb65345,blue:0x4f818f,gold:0xb8954b,green:0x627f68,ground:0xdedfd8,walk:0xe9e3d6,building:0xa9b0ab};
const state={area:0,ai:false,az:.88,el:.55,dist:22,drag:false,last:[0,0]};
const host=document.getElementById('scene'),status=document.getElementById('status'),fallback=document.getElementById('fallback'),title=document.getElementById('areaTitle'),mode=document.getElementById('modeTitle');
let renderer,scene,camera,root;
function setStatus(s){status.textContent=s} function mat(c,o=1){return new MeshStandardMaterial({color:c,roughness:.82,metalness:.02,transparent:o<1,opacity:o})}
function box(x,z,w,d,h,c,o=1){const m=new Mesh(new BoxGeometry(w,h,d),mat(c,o));m.position.set(x,h/2,z);m.castShadow=true;m.receiveShadow=true;return m}
function strip(x,z,w,d,c,h=.08,o=1){const m=box(x,z,w,d,h,c,o);m.position.y=h/2+.02;return m}
function tree(x,z){const g=new Group();g.add(box(x,z,.14,.14,1.3,0x6f5c48));const cr=new Mesh(new SphereGeometry(.65,10,8),mat(C.green));cr.position.set(x,1.75,z);g.add(cr);return g}
function label(s,x,z){const cv=document.createElement('canvas');cv.width=512;cv.height=128;const c=cv.getContext('2d');c.fillStyle='rgba(255,255,255,.94)';c.fillRect(0,0,512,128);c.fillStyle='#26312d';c.font='bold 40px sans-serif';c.fillText(s,18,72);const sp=new Sprite(new SpriteMaterial({map:new CanvasTexture(cv),transparent:true}));sp.scale.set(4,1,1);sp.position.set(x,1.35,z);return sp}
function people(){const g=new Group();for(let i=0;i<22;i++)g.add(box(-6+i*.58,-2+(i%4)*.38,.11,.11,.55,C.ink));return g}
function base(a){root.add(strip(0,0,18,11,C.ground,.12));root.add(strip(0,1.8,15,1.2,C.walk,.16));root.add(strip(0,-1.1,14,.8,0xc6d8c9,.14));for(let i=0;i<9;i++)root.add(tree(-6.2+i*1.55,-1.1));root.add(people());const ac=a.accent==='blue'?C.blue:a.accent==='gold'?C.gold:C.red;
 if(a.id==='zhong'){root.add(box(-4,-2.8,4,2.2,3.2,C.building));root.add(box(4,-2.6,4.3,2.3,3.6,C.building));root.add(box(0,3.2,3.6,2,2.5,0xb8bfba));root.add(strip(2.9,.3,4.2,2.3,0xcbd9dc,.18,.7));root.add(label('Bounded Test',2.8,.3));root.add(strip(-2.7,2.7,4.4,.55,ac,.13));root.add(label('Ordinary Bypass',-2.7,2.7));}
 else if(a.id==='origin'){[[-4,-2.6],[0,-2.9],[4,-2.5],[-2,3],[2.4,3.2]].forEach(([x,z],i)=>root.add(box(x,z,2.6,1.8,2.2+(i%2)*.4,0xbdb49a)));root.add(strip(0,.3,4,2.3,0xe2dbc0,.15));root.add(label('Inclusive Court',0,.3));root.add(strip(0,2.3,11,.5,ac,.13));root.add(label('Accessible Spine',0,2.3));}
 else{for(let i=0;i<6;i++)root.add(box(-5.8+i*2.2,-2.8+(i%2)*.25,1.6,1.3,1.7,0xc39f87));root.add(strip(0,1.2,12,1.25,0xd8cdbb,.15));root.add(label('Market Street',0,1.2));root.add(strip(3.6,3.1,3.6,1.1,0xcdd2cd,.15));root.add(label('Rider Pocket',3.6,3.1));} return ac;}
function ai(){if(!state.ai)return;const g=new Group();g.add(strip(-3.9,-.2,2.3,1.5,C.blue,.22,.45),strip(0,-.2,2.3,1.5,C.gold,.22,.45),strip(3.9,-.2,2.3,1.5,C.red,.22,.45),label('Ambient',-3.9,-.2),label('Consent',0,-.2),label('Bounded',3.9,-.2));root.add(g)}
function rebuild(){while(root.children.length)root.remove(root.children[0]);const a=DATA.areas[state.area];base(a);ai();title.textContent=`${a.zh} / ${a.en}`;mode.textContent=state.ai?'AI ON · optional capability':'AI OFF · permanent civic baseline';render()}
function cam(){camera.position.set(Math.cos(state.az)*Math.cos(state.el)*state.dist,Math.sin(state.el)*state.dist,Math.sin(state.az)*Math.cos(state.el)*state.dist);camera.lookAt(0,.4,0)} function render(){cam();renderer.render(scene,camera)}
function bind(){document.querySelectorAll('[data-area]').forEach(b=>b.onclick=()=>{state.area=+b.dataset.area;document.querySelectorAll('[data-area]').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));rebuild()});document.querySelectorAll('[data-ai]').forEach(b=>b.onclick=()=>{state.ai=b.dataset.ai==='on';document.querySelectorAll('[data-ai]').forEach(x=>x.setAttribute('aria-pressed',String((x.dataset.ai==='on')===state.ai)));rebuild()});window.onkeydown=e=>{if(['1','2','3'].includes(e.key)){state.area=+e.key-1;rebuild()}if(e.key.toLowerCase()==='o'){state.ai=false;rebuild()}if(e.key.toLowerCase()==='i'){state.ai=true;rebuild()}if(e.key.toLowerCase()==='r'){state.az=.88;state.el=.55;state.dist=22;render()}};renderer.domElement.onpointerdown=e=>{state.drag=true;state.last=[e.clientX,e.clientY];renderer.domElement.setPointerCapture(e.pointerId)};renderer.domElement.onpointerup=()=>state.drag=false;renderer.domElement.onpointermove=e=>{if(!state.drag)return;const dx=e.clientX-state.last[0],dy=e.clientY-state.last[1];state.last=[e.clientX,e.clientY];state.az-=dx*.007;state.el=Math.max(.18,Math.min(1.2,state.el-dy*.006));render()};renderer.domElement.addEventListener('wheel',e=>{e.preventDefault();state.dist=Math.max(12,Math.min(38,state.dist+e.deltaY*.018));render()},{passive:false});window.onresize=()=>{camera.aspect=host.clientWidth/host.clientHeight;camera.updateProjectionMatrix();renderer.setSize(host.clientWidth,host.clientHeight,false);render()}}
function init(){try{setStatus('Initializing local Three.js…');renderer=new WebGLRenderer({antialias:true});renderer.setPixelRatio(Math.min(devicePixelRatio,1.5));renderer.setSize(host.clientWidth,host.clientHeight,false);renderer.shadowMap.enabled=true;renderer.outputColorSpace=SRGBColorSpace;host.prepend(renderer.domElement);scene=new Scene();scene.background=new Color(C.paper);camera=new PerspectiveCamera(42,host.clientWidth/host.clientHeight,.1,100);root=new Group();scene.add(root,new HemisphereLight(0xffffff,0x6f776f,2.1));const sun=new DirectionalLight(0xfff0d3,3);sun.position.set(8,14,-8);sun.castShadow=true;scene.add(sun);bind();rebuild();fallback.hidden=true;setStatus('LOCAL · OFFLINE · NO NETWORK')}catch(e){console.error(e);setStatus('WebGL unavailable · static fallback shown');fallback.hidden=false}}
init();
