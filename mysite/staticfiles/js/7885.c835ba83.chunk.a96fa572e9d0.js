"use strict";(self.webpackChunkparticles=self.webpackChunkparticles||[]).push([[7885],{7885:(i,t,o)=>{o.d(t,{OutOutMode:()=>s});var e=o(4409);class s{constructor(i){this.container=i,this.modes=["out"]}async update(i,t,o,s){if(!this.modes.includes(s))return;const n=this.container;switch(i.outType){case"inside":{const{x:t,y:o}=i.velocity,s=e.Mi.origin;s.length=i.moveCenter.radius,s.angle=i.velocity.angle+Math.PI,s.addTo(e.Mi.create(i.moveCenter));const{dx:a,dy:r}=(0,e.vr)(i.position,s);if(t<=0&&a>=0||o<=0&&r>=0||t>=0&&a<=0||o>=0&&r<=0)return;i.position.x=Math.floor((0,e.BH)({min:0,max:n.canvas.size.width})),i.position.y=Math.floor((0,e.BH)({min:0,max:n.canvas.size.height}));const{dx:p,dy:d}=(0,e.vr)(i.position,i.moveCenter);i.direction=Math.atan2(-d,-p),i.velocity.angle=i.direction;break}default:if((0,e.Tj)(i.position,n.canvas.size,e.Mi.origin,i.getRadius(),t))return;switch(i.outType){case"outside":{i.position.x=Math.floor((0,e.BH)({min:-i.moveCenter.radius,max:i.moveCenter.radius}))+i.moveCenter.x,i.position.y=Math.floor((0,e.BH)({min:-i.moveCenter.radius,max:i.moveCenter.radius}))+i.moveCenter.y;const{dx:t,dy:o}=(0,e.vr)(i.position,i.moveCenter);i.moveCenter.radius&&(i.direction=Math.atan2(o,t),i.velocity.angle=i.direction);break}case"normal":{const o=i.options.move.warp,s=n.canvas.size,a={bottom:s.height+i.getRadius()+i.offset.y,left:-i.getRadius()-i.offset.x,right:s.width+i.getRadius()+i.offset.x,top:-i.getRadius()-i.offset.y},r=i.getRadius(),p=(0,e.AE)(i.position,r);"right"===t&&p.left>s.width+i.offset.x?(i.position.x=a.left,i.initialPosition.x=i.position.x,o||(i.position.y=(0,e.G0)()*s.height,i.initialPosition.y=i.position.y)):"left"===t&&p.right<-i.offset.x&&(i.position.x=a.right,i.initialPosition.x=i.position.x,o||(i.position.y=(0,e.G0)()*s.height,i.initialPosition.y=i.position.y)),"bottom"===t&&p.top>s.height+i.offset.y?(o||(i.position.x=(0,e.G0)()*s.width,i.initialPosition.x=i.position.x),i.position.y=a.top,i.initialPosition.y=i.position.y):"top"===t&&p.bottom<-i.offset.y&&(o||(i.position.x=(0,e.G0)()*s.width,i.initialPosition.x=i.position.x),i.position.y=a.bottom,i.initialPosition.y=i.position.y);break}}}await Promise.resolve()}}}}]);
//# sourceMappingURL=7885.c835ba83.chunk.js.25d2924c7a90.map