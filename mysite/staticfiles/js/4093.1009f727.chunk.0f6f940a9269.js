"use strict";(self.webpackChunkparticles=self.webpackChunkparticles||[]).push([[4093],{4093:(n,t,e)=>{e.d(t,{Bouncer:()=>a});var i=e(4409);class o{constructor(){this.distance=200}load(n){n&&void 0!==n.distance&&(this.distance=n.distance)}}const s="bounce";class a extends i.sJ{constructor(n){super(n)}clear(){}init(){const n=this.container,t=n.actualOptions.interactivity.modes.bounce;t&&(n.retina.bounceModeDistance=t.distance*n.retina.pixelRatio)}async interact(){const n=this.container,t=n.actualOptions.interactivity.events,o=n.interactivity.status===i.Rb,a=t.onHover.enable,c=t.onHover.mode,r=t.onDiv;if(o&&a&&(0,i.hn)(s,c)){const{mouseBounce:n}=await e.e(6091).then(e.bind(e,6091));n(this.container,(n=>this.isEnabled(n)))}else{const{divBounce:n}=await e.e(6091).then(e.bind(e,6091));n(this.container,r,s,(n=>this.isEnabled(n)))}}isEnabled(n){var t;const e=this.container,o=e.actualOptions,a=e.interactivity.mouse,c=(null!==(t=null===n||void 0===n?void 0:n.interactivity)&&void 0!==t?t:o.interactivity).events,r=c.onDiv;return!!a.position&&c.onHover.enable&&(0,i.hn)(s,c.onHover.mode)||(0,i.iK)(s,r)}loadModeOptions(n){n.bounce||(n.bounce=new o);for(var t=arguments.length,e=new Array(t>1?t-1:0),i=1;i<t;i++)e[i-1]=arguments[i];for(const o of e)n.bounce.load(null===o||void 0===o?void 0:o.bounce)}reset(){}}}}]);
//# sourceMappingURL=4093.1009f727.chunk.js.00a974e0688a.map