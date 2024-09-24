"use strict";(self.webpackChunkparticles=self.webpackChunkparticles||[]).push([[1769],{1769:(t,i,e)=>{e.d(i,{Particle:()=>f});var s=e(9135),o=e(8164),a=e(2496),n=e(753),l=e(1189),r=e(6266),h=e(3849),c=e(6480),d=e(8802);const u=.5;function p(t){if(!(0,o.hn)(t.outMode,t.checkModes))return;const i=2*t.radius;t.coord>t.maxCoord-i?t.setCb(-t.radius):t.coord<i&&t.setCb(t.radius)}class f{constructor(t,i){var e=this;this.container=i,this._calcPosition=function(t,i,o){var a,n,l,r;let c=arguments.length>3&&void 0!==arguments[3]?arguments[3]:0;for(const[,s]of t.plugins){const t=void 0!==s.particlePosition?s.particlePosition(i,e):void 0;if(t)return h.p.create(t.x,t.y,o)}const d=t.canvas.size,u=(0,s.Nx)({size:d,position:i}),f=h.p.create(u.x,u.y,o),v=e.getRadius(),g=e.options.move.outModes,y=i=>{p({outMode:i,checkModes:["bounce"],coord:f.x,maxCoord:t.canvas.size.width,setCb:t=>f.x+=t,radius:v})},b=i=>{p({outMode:i,checkModes:["bounce"],coord:f.y,maxCoord:t.canvas.size.height,setCb:t=>f.y+=t,radius:v})};if(y(null!==(a=g.left)&&void 0!==a?a:g.default),y(null!==(n=g.right)&&void 0!==n?n:g.default),b(null!==(l=g.top)&&void 0!==l?l:g.default),b(null!==(r=g.bottom)&&void 0!==r?r:g.default),e._checkOverlap(f,c)){const i=1;return e._calcPosition(t,void 0,o,c+i)}return f},this._calculateVelocity=()=>{const t=(0,s.$m)(this.direction).copy(),i=this.options.move;if("inside"===i.direction||"outside"===i.direction)return t;const e=(0,s.pu)((0,s.VG)(i.angle.value)),o=(0,s.pu)((0,s.VG)(i.angle.offset)),a={left:o-e*u,right:o+e*u};return i.straight||(t.angle+=(0,s.U4)((0,s.DT)(a.left,a.right))),i.random&&"number"===typeof i.speed&&(t.length*=(0,s.G0)()),t},this._checkOverlap=function(t){let i=arguments.length>1&&void 0!==arguments[1]?arguments[1]:0;const o=e.options.collisions,n=e.getRadius();if(!o.enable)return!1;const l=o.overlap;if(l.enable)return!1;const r=l.retries;if(r>=0&&i>r)throw new Error("".concat(a.dI," particle is overlapping and can't be placed"));return!!e.container.particles.find((i=>(0,s.Yf)(t,i.position)<n+i.getRadius()))},this._getRollColor=t=>{var i;if(!t||!this.roll||!this.backColor&&!this.roll.alter)return t;const e=this.roll.horizontal&&this.roll.vertical?2:1,s=this.roll.horizontal?Math.PI*u:0;return Math.floor(((null!==(i=this.roll.angle)&&void 0!==i?i:0)+s)/(Math.PI/e))%2?this.backColor?this.backColor:this.roll.alter?(0,c.yx)(t,this.roll.alter.type,this.roll.alter.value):t:t},this._initPosition=t=>{var i,e;const a=this.container,n=(0,s.VG)(this.options.zIndex.value);this.position=this._calcPosition(a,t,(0,s.qE)(n,0,a.zLayers)),this.initialPosition=this.position.copy();const l=a.canvas.size;switch(this.moveCenter={...(0,o.E9)(this.options.move.center,l),radius:null!==(i=this.options.move.center.radius)&&void 0!==i?i:0,mode:null!==(e=this.options.move.center.mode)&&void 0!==e?e:"percent"},this.direction=(0,s.JY)(this.options.move.direction,this.position,this.moveCenter),this.options.move.direction){case"inside":this.outType="inside";break;case"outside":this.outType="outside"}this.offset=r.M.origin},this._engine=t}destroy(t){var i;if(this.unbreakable||this.destroyed)return;this.destroyed=!0,this.bubble.inRange=!1,this.slow.inRange=!1;const e=this.container,s=this.pathGenerator,o=e.shapeDrawers.get(this.shape);null===o||void 0===o||null===(i=o.particleDestroy)||void 0===i||i.call(o,this);for(const[,l]of e.plugins){var a;null===(a=l.particleDestroyed)||void 0===a||a.call(l,this,t)}for(const l of e.particles.updaters){var n;null===(n=l.particleDestroyed)||void 0===n||n.call(l,this,t)}null===s||void 0===s||s.reset(this),this._engine.dispatchEvent("particleDestroyed",{container:this.container,data:{particle:this}})}async draw(t){const i=this.container,e=i.canvas;for(const[,s]of i.plugins)await e.drawParticlePlugin(s,this,t);await e.drawParticle(this,t)}getFillColor(){var t;return this._getRollColor(null!==(t=this.bubble.color)&&void 0!==t?t:(0,n.O_)(this.color))}getMass(){return this.getRadius()**2*Math.PI*u}getPosition(){return{x:this.position.x+this.offset.x,y:this.position.y+this.offset.y,z:this.position.z}}getRadius(){var t;return null!==(t=this.bubble.radius)&&void 0!==t?t:this.size.value}getStrokeColor(){var t;return this._getRollColor(null!==(t=this.bubble.color)&&void 0!==t?t:(0,n.O_)(this.strokeColor))}async init(t,i,e,r){var h,c,u,p,f,v,g,y,b,w,C;const m=this.container,z=this._engine;this.id=t,this.group=r,this.effectClose=!0,this.effectFill=!0,this.shapeClose=!0,this.shapeFill=!0,this.pathRotation=!1,this.lastPathTime=0,this.destroyed=!1,this.unbreakable=!1,this.rotation=0,this.misplaced=!1,this.retina={maxDistance:{}},this.outType="normal",this.ignoresResizeRatio=!0;const _=m.retina.pixelRatio,D=m.actualOptions,P=(0,d.y)(this._engine,m,D.particles),x=P.effect.type,k=P.shape.type,{reduceDuplicates:R}=P;this.effect=(0,o.TA)(x,this.id,R),this.shape=(0,o.TA)(k,this.id,R);const M=P.effect,G=P.shape;if(e){var I,T;if(null!==(I=e.effect)&&void 0!==I&&I.type){const t=e.effect.type,i=(0,o.TA)(t,this.id,R);i&&(this.effect=i,M.load(e.effect))}if(null!==(T=e.shape)&&void 0!==T&&T.type){const t=e.shape.type,i=(0,o.TA)(t,this.id,R);i&&(this.shape=i,G.load(e.shape))}}this.effectData=function(t,i,e,s){const a=i.options[t];if(a)return(0,o.zw)({close:i.close,fill:i.fill},(0,o.TA)(a,e,s))}(this.effect,M,this.id,R),this.shapeData=function(t,i,e,s){const a=i.options[t];if(a)return(0,o.zw)({close:i.close,fill:i.fill},(0,o.TA)(a,e,s))}(this.shape,G,this.id,R),P.load(e);const V=this.effectData;V&&P.load(V.particles);const E=this.shapeData;E&&P.load(E.particles);const A=new l.k(z,m);A.load(m.actualOptions.interactivity),A.load(P.interactivity),this.interactivity=A,this.effectFill=null!==(h=null===V||void 0===V?void 0:V.fill)&&void 0!==h?h:P.effect.fill,this.effectClose=null!==(c=null===V||void 0===V?void 0:V.close)&&void 0!==c?c:P.effect.close,this.shapeFill=null!==(u=null===E||void 0===E?void 0:E.fill)&&void 0!==u?u:P.shape.fill,this.shapeClose=null!==(p=null===E||void 0===E?void 0:E.close)&&void 0!==p?p:P.shape.close,this.options=P;const F=this.options.move.path;this.pathDelay=(0,s.VG)(F.delay.value)*a.Xu,F.generator&&(this.pathGenerator=this._engine.getPathGenerator(F.generator),this.pathGenerator&&m.addPath(F.generator,this.pathGenerator)&&await this.pathGenerator.init(m)),m.retina.initParticle(this),this.size=(0,o.Xs)(this.options.size,_),this.bubble={inRange:!1},this.slow={inRange:!1,factor:1},this._initPosition(i),this.initialVelocity=this._calculateVelocity(),this.velocity=this.initialVelocity.copy();this.moveDecay=1-(0,s.VG)(this.options.move.decay);const O=m.particles;O.setLastZIndex(this.position.z),this.zIndexFactor=this.position.z/m.zLayers,this.sides=24;let S=m.effectDrawers.get(this.effect);S||(S=this._engine.getEffectDrawer(this.effect),S&&m.effectDrawers.set(this.effect,S)),null!==(f=S)&&void 0!==f&&f.loadEffect&&await S.loadEffect(this);let L=m.shapeDrawers.get(this.shape);L||(L=this._engine.getShapeDrawer(this.shape),L&&m.shapeDrawers.set(this.shape,L)),null!==(v=L)&&void 0!==v&&v.loadShape&&await L.loadShape(this);const N=null===(g=L)||void 0===g?void 0:g.getSidesCount;N&&(this.sides=N(this)),this.spawning=!1,this.shadowColor=(0,n.BN)(this.options.shadow.color);for(const s of O.updaters)await s.init(this);for(const s of O.movers){var X;await(null===(X=s.init)||void 0===X?void 0:X.call(s,this))}await(null===(y=S)||void 0===y||null===(b=y.particleInit)||void 0===b?void 0:b.call(y,m,this)),await(null===(w=L)||void 0===w||null===(C=w.particleInit)||void 0===C?void 0:C.call(w,m,this));for(const[,s]of m.plugins){var Y;null===(Y=s.particleCreated)||void 0===Y||Y.call(s,this)}}isInsideCanvas(){const t=this.getRadius(),i=this.container.canvas.size,e=this.position;return e.x>=-t&&e.y>=-t&&e.y<=i.height+t&&e.x<=i.width+t}isVisible(){return!this.destroyed&&!this.spawning&&this.isInsideCanvas()}reset(){for(const i of this.container.particles.updaters){var t;null===(t=i.reset)||void 0===t||t.call(i,this)}}}}}]);
//# sourceMappingURL=1769.9f08e96d.chunk.js.map