(window.webpackJsonp=window.webpackJsonp||[]).push([[10],{"+2cr":function(e,t,n){"use strict";(function(e){var a=n("sL3o"),o=n("C+Gs"),i=n("Ajgj"),r=n("+mXV"),s=n("ucLl"),c=n("kaPt");const l=Object(o.a)({ctftimeButton:{"& button":{borderColor:"#d9d9d9 !important"}}},({classes:t,ctftimeId:n,onUpdate:o})=>{const{toast:l}=Object(s.b)(),d=Object(r.a)(async({ctftimeToken:e,ctftimeId:t})=>{const{kind:n,message:a}=await Object(i.e)({ctftimeToken:e});"goodCtftimeAuthSet"===n?o({ctftimeId:t}):l({body:a,type:"error"})},[l,o]),u=Object(r.a)(async()=>{const{kind:e,message:t}=await Object(i.b)();"goodCtftimeRemoved"===e?o({ctftimeId:null}):l({body:t,type:"error"})},[l,o]);return e("div",{class:"card"},e("div",{class:"content"},e("p",null,"CTFtime Integration"),null===n?e(a.Fragment,null,e("p",{class:"font-thin u-no-margin"},"To login with CTFtime and get a badge on your profile, connect CTFtime to your account."),e("div",{class:"row u-center"},e(c.a,{class:t.ctftimeButton,onCtftimeDone:d}))):e(a.Fragment,null,e("p",{class:"font-thin u-no-margin"},"Your account is already connected to CTFtime. You can disconnect CTFtime from your account."),e("div",{class:"row u-center"},e("button",{class:"btn-info u-center",onClick:u},"Remove")))))});t.a=l}).call(this,n("sL3o").h)},"2L4n":function(e,t,n){"use strict";function a(e){return Object(o.h)(l.a,{...e,glyph:"eds_group",viewBox:"0 0 24 24"})}n.d(t,"a",(function(){return a}));var o=n("sL3o"),i=n("ziER"),r=n.n(i),s=n("5JeM"),c=n.n(s),l=n("VXtC");const d=new r.a({id:"eds_group",use:"eds_group-usage",viewBox:"0 0 24 24",content:'<symbol viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" fill="#ffffff" id="eds_group"><path fill-rule="evenodd" clip-rule="evenodd" d="M9 12c1.93 0 3.5-1.57 3.5-3.5S10.93 5 9 5 5.5 6.57 5.5 8.5 7.07 12 9 12zm-7 5.25c0-2.33 4.66-3.5 7-3.5s7 1.17 7 3.5V19H2v-1.75zm7-1.5c-1.79 0-3.82.67-4.66 1.25h9.32c-.84-.58-2.87-1.25-4.66-1.25zm1.5-7.25C10.5 7.67 9.83 7 9 7s-1.5.67-1.5 1.5S8.17 10 9 10s1.5-.67 1.5-1.5zm5.54 5.31c1.16.84 1.96 1.96 1.96 3.44V19h4v-1.75c0-2.02-3.5-3.17-5.96-3.44zM18.5 8.5c0 1.93-1.57 3.5-3.5 3.5-.54 0-1.04-.13-1.5-.35.63-.89 1-1.98 1-3.15s-.37-2.26-1-3.15c.46-.22.96-.35 1.5-.35 1.93 0 3.5 1.57 3.5 3.5z" /></symbol>'});c.a.add(d)},"38Gp":function(e,t,n){"use strict";n.r(t),function(e){function a(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);t&&(a=a.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,a)}return n}function o(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?a(Object(n),!0).forEach((function(t){i(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):a(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function i(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}var r=n("+mXV"),s=n("Xjb4"),c=n("obyI"),l=n("C+Gs"),d=n("O1lG"),u=n("ucLl"),m=n("f/Gm"),p=n("hClm"),f=n("+2cr"),b=n("a/8j"),v=n("6WUA"),h=n("4WT4"),g=n("YfLz"),w=n("ZvEd"),y=n("2L4n"),j=n("Fzg7"),O=n("MkB2"),x=n("q9Eb"),C=n("fHzH");const k=Object(s.b)(Object(l.a)({icon:{"& svg":{verticalAlign:"middle",height:"1.25em",fill:"#333"},marginRight:"1.5em"},publicHeader:{textOverflow:"ellipsis",overflow:"hidden",margin:"0 !important",maxWidth:"75vw"},privateHeader:{textOverflow:"ellipsis",overflow:"hidden",margin:"0 !important",maxWidth:"30vw"},"@media (max-width: 804px)":{privateHeader:{maxWidth:"75vw"}},wrapper:{display:"flex",justifyContent:"space-between",paddingTop:"15px",paddingBottom:"5px"}},({name:t,score:n,division:a,divisionPlace:o,globalPlace:i,ctftimeId:r,classes:s,isPrivate:c})=>e("div",{class:"card"},e("div",{class:"content"},e("div",{class:s.wrapper},e("h5",{class:"title "+(c?s.privateHeader:s.publicHeader),title:t},t),r&&e("a",{href:"https://ctftime.org/team/"+r,target:"_blank",rel:"noopener noreferrer"},e(x.a,{style:"height: 20px;"}))),e("div",{class:"action-bar"},e("p",null,e("span",{class:"icon "+s.icon},e(g.a,null)),0===n?"No points earned":n+" total points"),e("p",null,e("span",{class:"icon "+s.icon},e(O.a,{style:"height: 24px;"})),0===n?"Unranked":`${o} in the ${a} division`),e("p",null,e("span",{class:"icon "+s.icon},e(O.a,{style:"height: 24px;"})),0===n?"Unranked":i+" across all teams"),e("p",null,e("span",{class:"icon "+s.icon},e(w.a,{style:"height: 24px;"})),a," division")))))),z=Object(l.a)({btn:{marginRight:"10px"}},({teamToken:t,classes:n})=>{const{toast:a}=Object(u.b)(),o=`${location.origin}/login?token=${encodeURIComponent(t)}`,[i,s]=Object(r.j)(!1),c=Object(r.a)(()=>s(!i),[i]),l=Object(r.a)(()=>{if(navigator.clipboard)try{navigator.clipboard.writeText(o).then(()=>{a({body:"Copied team invite URL to clipboard"})})}catch(e){}},[a,o]);return e("div",{class:"card"},e("div",{class:"content"},e("p",null,"Team Invite"),e("p",{class:"font-thin"},"Send this team invite URL to your teammates so they can login."),e("button",{onClick:l,class:n.btn+" btn-info u-center",name:"btn",value:"submit",type:"submit"},"Copy"),e("button",{onClick:c,class:"btn-info u-center",name:"btn",value:"submit",type:"submit"},i?"Hide":"Reveal"),i&&e(v.a,{token:o})))}),L=Object(l.a)({form:{"& button":{margin:0,marginBottom:"0.4em",float:"right"},padding:"0 !important"},divisionSelect:{paddingLeft:"2.75rem"},recaptchaLegalNotice:{marginTop:"20px"}},({name:t,email:n,divisionId:a,allowedDivisions:o,onUpdate:i,classes:s})=>{const{toast:l}=Object(u.b)(),p=Object(C.b)("setEmail"),[f,b]=Object(r.j)(t),v=Object(r.a)(e=>b(e.target.value),[]),[h,g]=Object(r.j)(n),O=Object(r.a)(e=>g(e.target.value),[]),[x,k]=Object(r.j)(a),z=Object(r.a)(e=>k(e.target.value),[]),[L,M]=Object(r.j)(!1),T=Object(r.a)(async e=>{e.preventDefault();let o=!1;if(f!==t||x!==a){o=!0,M(!0);const{error:e,data:n}=await Object(d.e)({name:t===f?void 0:f,division:a===x?void 0:x});if(M(!1),void 0!==e)return void l({body:e,type:"error"});l({body:"Profile updated"}),i({name:n.user.name,divisionId:n.user.division})}if(h!==n){let e,t;if(o=!0,""===h)M(!0),({error:e,data:t}=await Object(d.a)());else{const n=await(null==p?void 0:p());M(!0),({error:e,data:t}=await Object(d.f)({email:h,recaptchaCode:n}))}if(M(!1),void 0!==e)return void l({body:e,type:"error"});l({body:t}),i({email:h})}o||l({body:"Nothing to update!"})},[f,h,x,t,n,a,i,l,p]);return e("div",{class:"card"},e("div",{class:"content"},e("p",null,"Update Information"),e("p",{class:"font-thin u-no-margin"},"This will change how your team appears on the scoreboard. You may only change your team's name once every 10 minutes."),e("div",{class:"row u-center"},e(m.a,{class:"col-12 "+s.form,onSubmit:T,disabled:L,buttonText:"Update"},e("input",{required:!0,autocomplete:"username",autocorrect:"off",maxLength:"64",minLength:"2",icon:e(y.a,{style:"height: 24px;"}),name:"name",placeholder:"Team Name",type:"text",value:f,onChange:v}),e("input",{autocomplete:"email",autocorrect:"off",icon:e(j.a,{style:"height: 24px;"}),name:"email",placeholder:"Email",type:"email",value:h,onChange:O}),e("select",{icon:e(w.a,{style:"height: 24px;"}),class:"select "+s.divisionSelect,name:"division",value:x,onChange:z},e("option",{value:"",disabled:!0},"Division"),o.map(t=>e("option",{key:t,value:t},c.a.divisions[t])))),p&&e("div",{class:s.recaptchaLegalNotice},e(C.a,null)))))});t.default=Object(l.a)({root:{display:"grid",gridTemplateColumns:"repeat(auto-fit, minmax(384px, 1fr))",width:"100%",maxWidth:"1500px",margin:"auto","& .card":{background:"#243746",marginBottom:"20px"},"& input, & select, & option":{background:"rgba(0, 0, 0, 0.28)",color:"#fff !important"}},col:{margin:"0 auto",width:"calc(100% - 20px)",marginLeft:"10px"},privateCol:{width:"calc(100% - 20px)",marginLeft:"10px"},errorCard:{background:"#243746"}},({uuid:t,classes:n})=>{const[a,i]=Object(r.j)(!1),[s,l]=Object(r.j)(null),[m,v]=Object(r.j)({}),{toast:g}=Object(u.b)(),{name:w,email:y,division:j,score:O,solves:x,teamToken:C,ctftimeId:M,allowedDivisions:T}=m,P=c.a.divisions[m.division],_=h.b.placementString(m.divisionPlace),E=h.b.placementString(m.globalPlace),S=void 0===t||"me"===t;Object(r.d)(()=>{i(!1),S?Object(d.c)().then(({data:e,error:t})=>{t?g({body:t,type:"error"}):v(e),i(!0)}):Object(d.d)(t).then(({data:e,error:t})=>{t?l("Profile not found"):v(e),i(!0)})},[t,S,g]);const B=Object(r.a)(({name:e,email:t,divisionId:n,ctftimeId:a})=>{v(i=>o(o({},i),{},{name:void 0===e?i.name:e,email:void 0===t?i.email:t,division:void 0===n?i.division:n,ctftimeId:void 0===a?i.ctftimeId:a}))},[]);return Object(r.d)(()=>{document.title="Profile | "+c.a.ctfName},[]),a?null!==s?e("div",{class:"row u-center"},e("div",{class:"col-4"},e("div",{class:"card "+n.errorCard},e("div",{class:"content"},e("p",{class:"title"},"There was an error"),e("p",{class:"font-thin"},s))))):e("div",{class:n.root},S&&e("div",{class:n.privateCol},e(z,{teamToken:C}),e(L,{name:w,email:y,divisionId:j,allowedDivisions:T,onUpdate:B}),c.a.ctftime&&e(f.a,{ctftimeId:M,onUpdate:B})),e("div",{class:n.col},e(k,{name:w,score:O,division:P,divisionPlace:_,globalPlace:E,ctftimeId:M,isPrivate:S}),S&&c.a.userMembers&&e(p.a,null),e(S?b.a:b.b,{solves:x}))):null})}.call(this,n("sL3o").h)},"6WUA":function(e,t,n){"use strict";(function(e){function a(){return(a=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var n=arguments[t];for(var a in n)Object.prototype.hasOwnProperty.call(n,a)&&(e[a]=n[a])}return e}).apply(this,arguments)}function o(e,t){if(null==e)return{};var n,a,o=function(e,t){if(null==e)return{};var n,a,o={},i=Object.keys(e);for(a=0;a<i.length;a++)t.indexOf(n=i[a])>=0||(o[n]=e[n]);return o}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(a=0;a<i.length;a++)t.indexOf(n=i[a])>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(o[n]=e[n])}return o}var i=n("C+Gs");t.a=Object(i.a)({quote:{fontSize:"small",overflowWrap:"break-word",userSelect:"all",fontFamily:"monospace !important",cursor:"pointer",background:"#111"}},t=>{let{classes:n,token:i}=t,r=o(t,["classes","token"]);return e("blockquote",a({class:n.quote},r),i)})}).call(this,n("sL3o").h)},Fzg7:function(e,t,n){"use strict";function a(e){return Object(o.h)(l.a,{...e,glyph:"eds_email_draft",viewBox:"0 0 24 24"})}n.d(t,"a",(function(){return a}));var o=n("sL3o"),i=n("ziER"),r=n.n(i),s=n("5JeM"),c=n.n(s),l=n("VXtC");const d=new r.a({id:"eds_email_draft",use:"eds_email_draft-usage",viewBox:"0 0 24 24",content:'<symbol viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" fill="#ffffff" id="eds_email_draft"><path fill-rule="evenodd" clip-rule="evenodd" d="M21.99 9.5c0-.72-.37-1.35-.94-1.7L12 2.5 2.95 7.8c-.57.35-.95.98-.95 1.7v10c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2l-.01-10zm-2 0v.01L12 14.5l-8-5 8-4.68 7.99 4.68zM4 11.84v7.66h16l-.01-7.63L12 16.86l-8-5.02z" /></symbol>'});c.a.add(d)},JltG:function(e,t,n){"use strict";n.d(t,"a",(function(){return o})),n.d(t,"b",(function(){return i}));const a=e=>{const t=new Date(e);return`${t.toLocaleDateString()} ${t.toLocaleTimeString()}`},o=e=>{const t=new Date(e).getTimezoneOffset(),n=String(Math.floor(Math.abs(t)/60)).padStart(2,"0"),o=String(Math.abs(t)%60).padStart(2,"0"),i=t>0?"-":"+";return`${a(e)} UTC${i}${n}:${o}`},i=e=>{const t=Date.now()-e,n=Math.floor(t/1e3);if(n<60)return"just now";const o=Math.floor(n/60);if(o<60)return`${o} minute${1===o?"":"s"} ago`;const i=Math.floor(o/60);if(i<24)return`${i} hour${1===i?"":"s"} ago`;const r=Math.floor(i/24);return r<7?`${r} day${1===r?"":"s"} ago`:a(e)}},MkB2:function(e,t,n){"use strict";function a(e){return Object(o.h)(l.a,{...e,glyph:"eds_bar_chart",viewBox:"0 0 24 24"})}n.d(t,"a",(function(){return a}));var o=n("sL3o"),i=n("ziER"),r=n.n(i),s=n("5JeM"),c=n.n(s),l=n("VXtC");const d=new r.a({id:"eds_bar_chart",use:"eds_bar_chart-usage",viewBox:"0 0 24 24",content:'<symbol viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" fill="#ffffff" id="eds_bar_chart"><path fill-rule="evenodd" clip-rule="evenodd" d="M10.6 5h2.8v14h-2.8V5zM5 9.2h3V19H5V9.2zM19 13h-2.8v6H19v-6z" /></symbol>'});c.a.add(d)},O1lG:function(e,t,n){"use strict";n.d(t,"c",(function(){return o})),n.d(t,"b",(function(){return i})),n.d(t,"d",(function(){return r})),n.d(t,"e",(function(){return s})),n.d(t,"f",(function(){return c})),n.d(t,"a",(function(){return l}));var a=n("vgrf");const o=async()=>{const e=await Object(a.b)("GET","/users/me");return Object(a.a)({resp:e,valid:["goodUserData"]})},i=async({authToken:e})=>{const{data:t}=await(await fetch("/api/v1/users/me",{headers:{authorization:"Bearer "+e}})).json();return t},r=async e=>{const t=await Object(a.b)("GET","/users/"+encodeURIComponent(e));return Object(a.a)({resp:t,valid:["goodUserData"]})},s=async({name:e,division:t})=>{const n=await Object(a.b)("PATCH","/users/me",{name:e,division:t});if("badRateLimit"===n.kind){const e=Math.floor(n.data.timeLeft/1e3),t=Math.floor(e/60);let a;return a=0===t?e+" seconds":t+" minutes",{error:`Please wait ${a} before trying this again`}}return Object(a.a)({resp:n,valid:["goodUserUpdate"]})},c=async({email:e,recaptchaCode:t})=>{const n=await Object(a.b)("PUT","/users/me/auth/email",{email:e,recaptchaCode:t});return Object(a.a)({resp:n,valid:["goodVerifySent","goodEmailSet"],resolveDataMessage:!0})},l=async()=>{const e=await Object(a.b)("DELETE","/users/me/auth/email");return Object(a.a)({resp:e,valid:["goodEmailRemoved","badEmailNoExists"],resolveDataMessage:!0})}},QMbY:function(e,t,n){"use strict";var a=n("obyI");t.a=()=>{const e=Array.from(crypto.getRandomValues(new Uint8Array(16))).map(e=>e.toString(16).padStart(2,"0")).join("");return(({url:e,title:t,w:n,h:a})=>{const o=window.innerWidth/window.screen.availWidth,i=(window.innerWidth-n)/2/o+window.screenLeft,r=(window.innerHeight-a)/2/o+window.screenTop;window.open(e,t,["scrollbars","resizable","width="+n/o,"height="+a/o,"top="+r,"left="+i].join(",")).focus()})({url:"https://oauth.ctftime.org/authorize?scope="+encodeURIComponent("team:read")+"&client_id="+encodeURIComponent(a.a.ctftime.clientId)+"&redirect_uri="+encodeURIComponent(location.origin+"/integrations/ctftime/callback")+"&state="+encodeURIComponent(e),title:"CTFtime",w:600,h:500}),e}},VXtC:function(e,t,n){"use strict";(function(e){function a(){return(a=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var n=arguments[t];for(var a in n)Object.prototype.hasOwnProperty.call(n,a)&&(e[a]=n[a])}return e}).apply(this,arguments)}function o(e,t){if(null==e)return{};var n,a,o=function(e,t){if(null==e)return{};var n,a,o={},i=Object.keys(e);for(a=0;a<i.length;a++)t.indexOf(n=i[a])>=0||(o[n]=e[n]);return o}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(a=0;a<i.length;a++)t.indexOf(n=i[a])>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(o[n]=e[n])}return o}function i(t){let{glyph:n,viewBox:i}=t,r=o(t,["glyph","viewBox"]);return e("svg",a({},r,{viewBox:i,xmlns:"http://www.w3.org/2000/svg"}),e("use",{xlinkHref:"#"+n}))}n.d(t,"a",(function(){return i}))}).call(this,n("sL3o").h)},YfLz:function(e,t,n){"use strict";function a(e){return Object(o.h)(l.a,{...e,glyph:"trophy",viewBox:"0 0 576 512"})}n.d(t,"a",(function(){return a}));var o=n("sL3o"),i=n("ziER"),r=n.n(i),s=n("5JeM"),c=n.n(s),l=n("VXtC");const d=new r.a({id:"trophy",use:"trophy-usage",viewBox:"0 0 576 512",content:'<symbol xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" fill="#ffffff" id="trophy"><path d="M552 64H448V24c0-13.3-10.7-24-24-24H152c-13.3 0-24 10.7-24 24v40H24C10.7 64 0 74.7 0 88v56c0 35.7 22.5 72.4 61.9 100.7 31.5 22.7 69.8 37.1 110 41.7C203.3 338.5 240 360 240 360v72h-48c-35.3 0-64 20.7-64 56v12c0 6.6 5.4 12 12 12h296c6.6 0 12-5.4 12-12v-12c0-35.3-28.7-56-64-56h-48v-72s36.7-21.5 68.1-73.6c40.3-4.6 78.6-19 110-41.7 39.3-28.3 61.9-65 61.9-100.7V88c0-13.3-10.7-24-24-24zM99.3 192.8C74.9 175.2 64 155.6 64 144v-16h64.2c1 32.6 5.8 61.2 12.8 86.2-15.1-5.2-29.2-12.4-41.7-21.4zM512 144c0 16.1-17.7 36.1-35.3 48.8-12.5 9-26.7 16.2-41.8 21.4 7-25 11.8-53.6 12.8-86.2H512v16z" /></symbol>'});c.a.add(d)},ZvEd:function(e,t,n){"use strict";function a(e){return Object(o.h)(l.a,{...e,glyph:"eds_users_circle",viewBox:"0 0 24 24"})}n.d(t,"a",(function(){return a}));var o=n("sL3o"),i=n("ziER"),r=n.n(i),s=n("5JeM"),c=n.n(s),l=n("VXtC");const d=new r.a({id:"eds_users_circle",use:"eds_users_circle-usage",viewBox:"0 0 24 24",content:'<symbol fill="#ffffff" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" id="eds_users_circle"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm.51 7.99c0-1.65-1.35-3-3-3s-3 1.35-3 3 1.35 3 3 3 3-1.35 3-3zm-3 1c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1zm8.5 0c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2-.01-1.11.89-2 2-2 1.11 0 2 .89 2 2zM9.51 16c-1.39 0-2.98.57-3.66 1.11a7.935 7.935 0 005.66 2.86v-2.78c0-1.89 2.98-2.7 4.5-2.7.88 0 2.24.28 3.24.87.48-1.03.75-2.17.75-3.37 0-4.41-3.59-8-8-8s-8 3.59-8 8c0 1.23.28 2.39.78 3.43 1.34-.98 3.43-1.43 4.73-1.43.44 0 .97.06 1.53.16-.63.57-1.06 1.22-1.3 1.86-.041 0-.083-.003-.123-.005A1.646 1.646 0 009.51 16z" /></symbol>'});c.a.add(d)},"a/8j":function(e,t,n){"use strict";(function(e){n.d(t,"b",(function(){return c})),n.d(t,"a",(function(){return l}));var a=n("sL3o"),o=n("C+Gs"),i=n("JltG"),r=n("mMF5");const s=t=>Object(o.a)({root:{display:"grid",padding:"20px",paddingTop:"0",gridTemplateColumns:"repeat(4, minmax(max-content, 1fr))","& div":{margin:"auto",padding:"10px"}},title:{gridColumn:"1 / -1",margin:"20px auto !important"},label:{borderBottom:"1px solid #fff",width:"100%",textAlign:"center"},inlineLabel:{display:"none"},icon:{width:"60px",margin:"auto !important"},[`@media (max-width: ${t?"1500px":"800px"})`]:{inlineLabel:{display:"initial",borderRight:"1px solid #fff"},root:{gridTemplateColumns:"repeat(2, minmax(max-content, 1fr))","& div":{margin:"0"}},label:{display:"none"},category:{borderTop:"1px solid #fff"}}},({classes:t,solves:n})=>e("div",{class:"card "+t.root},0===n.length?e("div",{class:t.title},e("div",{class:t.icon},e(r.a,null)),e("h5",null,"This team has no solves.")):e(a.Fragment,null,e("h5",{class:"title "+t.title},"Solves"),e("div",{class:t.label},"Category"),e("div",{class:t.label},"Challenge"),e("div",{class:t.label},"Solve time"),e("div",{class:t.label},"Points"),n.map(n=>e(a.Fragment,{key:n.id},e("div",{class:`${t.inlineLabel} ${t.category}`},"Category"),e("div",{class:t.category},n.category),e("div",{class:t.inlineLabel},"Name"),e("div",null,n.name),e("div",{class:t.inlineLabel},"Solve time"),e("div",null,Object(i.b)(n.createdAt)),e("div",{class:t.inlineLabel},"Points"),e("div",null,n.points)))))),c=s(!1),l=s(!0)}).call(this,n("sL3o").h)},azwp:function(e,t,n){"use strict";n.d(t,"b",(function(){return o})),n.d(t,"a",(function(){return i})),n.d(t,"c",(function(){return r}));var a=n("vgrf");const o=async()=>(await Object(a.b)("GET","/users/me/members")).data,i=async({email:e})=>{const t=await Object(a.b)("POST","/users/me/members",{email:e});switch(t.kind){case"badEmail":case"badKnownEmail":return{error:t.message};case"goodMemberCreate":return{data:t.data};default:return{error:"Unknown error"}}},r=async({id:e})=>(await Object(a.b)("DELETE","/users/me/members/"+encodeURIComponent(e))).data},"f/Gm":function(e,t,n){"use strict";(function(e){var a=n("C+Gs");t.a=Object(a.a)({root:{padding:"25px"},submit:{marginTop:"25px"},icon:{"& svg":{verticalAlign:"middle",height:"16px",fill:"#333"}}},t=>{const{classes:n,children:a,onSubmit:o,disabled:i,buttonText:r,errors:s}=t;return e("form",{onSubmit:o,class:t.class},[].concat(a).map(t=>{if(void 0===t.props)return;if(!t.props.name)return t;let{icon:a,error:o,name:i}=t.props;void 0!==s&&void 0!==i&&(o=o||s[i]);const r=void 0!==o;return t.props.class+=" input-contains-icon",r&&(t.props.class+=" input-error"),e("div",{class:"form-section",key:i},r&&e("label",{class:"text-danger info font-light"},o),e("div",{class:n.input+" input-control"},t,e("span",{class:"icon"},void 0!==a&&e("div",{class:"icon "+n.icon},a))))}),e("button",{disabled:i,class:n.submit+" btn-info u-center",name:"btn",value:"submit",type:"submit"},r),e("span",{class:"fg-danger info"}))})}).call(this,n("sL3o").h)},fHzH:function(e,t,n){"use strict";(function(e){n.d(t,"c",(function(){return m})),n.d(t,"d",(function(){return p})),n.d(t,"a",(function(){return f}));var a=n("obyI"),o=n("C+Gs"),i=n("+mXV");const r=[];let s,c;const l=async()=>{0!==r.length&&(await m()).execute(c)},d=async e=>{(await m()).reset(c);const{resolve:t}=r.shift();t(e),l()},u=async e=>{(await m()).reset(c);const{reject:t}=r.shift();t(e),l()},m=async()=>{var e,t;return s=null!=(e=s)?e:new Promise((e,t)=>{const n=document.createElement("script");n.src="https://www.google.com/recaptcha/api.js?render=explicit",n.addEventListener("load",()=>{window.grecaptcha.ready(()=>e(window.grecaptcha))}),n.addEventListener("error",t),document.body.appendChild(n)}),c=null!=(t=c)?t:(await s).render({theme:"dark",sitekey:a.a.recaptcha.siteKey,callback:d,"error-callback":u}),s},p=()=>new Promise((e,t)=>{r.push({resolve:e,reject:t}),l()}),f=Object(o.a)({root:{fontSize:"12px",textAlign:"center"},link:{display:"inline",padding:"0"}},({classes:t})=>e("div",{class:t.root},"This site is protected by reCAPTCHA.",e("br",null),"The Google"," ",e("a",{class:t.link,href:"https://policies.google.com/privacy",target:"_blank",rel:"noopener noreferrer"},"Privacy Policy")," ","and"," ",e("a",{class:t.link,href:"https://policies.google.com/terms",target:"_blank",rel:"noopener noreferrer"},"Terms of Service")," ","apply."));t.b=e=>{var t;const n=null==(t=a.a.recaptcha)?void 0:t.protectedActions.includes(e);Object(i.d)(()=>{n&&m()},[n]);const o=Object(i.a)(p,[]);if(n)return o}}).call(this,n("sL3o").h)},hClm:function(e,t,n){"use strict";(function(e){function a(){return(a=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var n=arguments[t];for(var a in n)Object.prototype.hasOwnProperty.call(n,a)&&(e[a]=n[a])}return e}).apply(this,arguments)}var o=n("C+Gs"),i=n("azwp"),r=n("+mXV"),s=n("f/Gm"),c=n("loEA"),l=n("ucLl");const d=Object(o.a)({root:{alignItems:"center",width:"100%",display:"flex",justifyContent:"space-between"}},({classes:t,id:n,email:a,setMembers:o})=>{const{toast:s}=Object(l.b)(),c=Object(r.a)(()=>{Object(i.c)({id:n}).then(()=>{o(e=>e.filter(e=>e.id!==n)),s({body:"Team member successfully deleted"})})},[n,o,s]);return e("div",{class:t.root,key:n},e("p",{class:"u-no-margin"},a),e("div",{class:"btn-container u-vertical-center"},e("input",{onClick:c,type:"submit",class:"btn-small btn-danger u-no-margin",value:"Delete"})))}),u=Object(o.a)({form:{"& button":{display:"block",marginLeft:"auto",marginRight:"0",marginTop:"10px"}}},({classes:t})=>{const{toast:n}=Object(l.b)(),[o,u]=Object(r.j)(""),m=Object(r.a)(e=>u(e.target.value),[]),[p,f]=Object(r.j)(!1),[b,v]=Object(r.j)([]),h=Object(r.a)(e=>{e.preventDefault(),f(!0),Object(i.a)({email:o}).then(({error:e,data:t})=>{f(!1),e?n({body:e,type:"error"}):(n({body:"Team member successfully added"}),v(e=>[...e,t]),u(""))})},[o,n]);return Object(r.d)(()=>{Object(i.b)().then(e=>v(e))},[]),e("div",{class:"card"},e("div",{class:"content"},e("p",null,"Team Information"),e("p",{class:"font-thin u-no-margin"},"Please enter a separate email for each team member. This data is collected for informational purposes only. Ensure that this section is up to date in order to remain prize eligible."),e("div",{class:"row u-center"},e(s.a,{class:"col-12 "+t.form,onSubmit:h,disabled:p,buttonText:"Add Member"},e("input",{required:!0,autocomplete:"email",autocorrect:"off",icon:e(c.a,{style:"height: 24px"}),name:"email",placeholder:"Email",type:"email",value:o,onChange:m})),0!==b.length&&e("div",{class:"row"},b.map(t=>e(d,a({setMembers:v},t)))))))});t.a=u}).call(this,n("sL3o").h)},kaPt:function(e,t,n){"use strict";(function(e){function a(e,t){if(null==e)return{};var n,a,o=function(e,t){if(null==e)return{};var n,a,o={},i=Object.keys(e);for(a=0;a<i.length;a++)t.indexOf(n=i[a])>=0||(o[n]=e[n]);return o}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(a=0;a<i.length;a++)t.indexOf(n=i[a])>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(o[n]=e[n])}return o}var o=n("sL3o"),i=n("q9Eb"),r=n("QMbY"),s=n("C+Gs"),c=n("Ajgj"),l=n("ucLl");t.a=Object(s.a)({ctftimeButton:{margin:"auto",lineHeight:"0",padding:"10px",background:"#243746","&:hover":{background:"#243746"},"& svg":{width:"150px"}}},Object(l.c)(class extends o.Component{constructor(...e){var t;super(...e),t=this,this.oauthState=null,this.handlePostMessage=async function(e){if(e.origin!==location.origin)return;if("ctftimeCallback"!==e.data.kind)return;if(null===t.oauthState||e.data.state!==t.oauthState)return;const{kind:n,message:a,data:o}=await Object(c.a)({ctftimeCode:e.data.ctftimeCode});"goodCtftimeToken"===n?t.props.onCtftimeDone(o):t.props.toast({body:a,type:"error"})},this.handleClick=()=>{this.oauthState=Object(r.a)()}}componentDidMount(){window.addEventListener("message",this.handlePostMessage)}componentWillUnmount(){window.removeEventListener("message",this.handlePostMessage)}render(t){let{classes:n}=t,o=a(t,["classes"]);return e("div",o,e("button",{class:n.ctftimeButton,onClick:this.handleClick},e(i.a,null)))}}))}).call(this,n("sL3o").h)},loEA:function(e,t,n){"use strict";function a(e){return Object(o.h)(l.a,{...e,glyph:"eds_person_add",viewBox:"0 0 24 24"})}n.d(t,"a",(function(){return a}));var o=n("sL3o"),i=n("ziER"),r=n.n(i),s=n("5JeM"),c=n.n(s),l=n("VXtC");const d=new r.a({id:"eds_person_add",use:"eds_person_add-usage",viewBox:"0 0 24 24",content:'<symbol fill="#ffffff" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" id="eds_person_add"><path fill-rule="evenodd" clip-rule="evenodd" d="M15 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0-6c1.1 0 2 .9 2 2s-.9 2-2 2-2-.9-2-2 .9-2 2-2zM7 18c0-2.66 5.33-4 8-4s8 1.34 8 4v2H7v-2zm2 0c.22-.72 3.31-2 6-2 2.7 0 5.8 1.29 6 2H9zm-3-6v3H4v-3H1v-2h3V7h2v3h3v2H6z" /></symbol>'});c.a.add(d)},mMF5:function(e,t,n){"use strict";function a(e){return Object(o.h)(l.a,{...e,glyph:"eds_timer",viewBox:"0 0 24 24"})}n.d(t,"a",(function(){return a}));var o=n("sL3o"),i=n("ziER"),r=n.n(i),s=n("5JeM"),c=n.n(s),l=n("VXtC");const d=new r.a({id:"eds_timer",use:"eds_timer-usage",viewBox:"0 0 24 24",content:'<symbol viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" fill="#ffffff" id="eds_timer"><path fill-rule="evenodd" clip-rule="evenodd" d="M9 1.505h6v2H9v-2zm2 13v-6h2v6h-2zm8.03-6.62 1.42-1.42c-.43-.51-.9-.99-1.41-1.41l-1.42 1.42A8.962 8.962 0 0 0 12 4.495a9 9 0 0 0-9 9c0 4.97 4.02 9 9 9s9-4.03 9-9c0-2.11-.74-4.06-1.97-5.61zM5 13.505c0 3.87 3.13 7 7 7s7-3.13 7-7-3.13-7-7-7-7 3.13-7 7z" /></symbol>'});c.a.add(d)},q9Eb:function(e,t,n){"use strict";function a(e){return Object(o.h)(l.a,{...e,glyph:"ctftime",viewBox:"0 0 283 80"})}n.d(t,"a",(function(){return a}));var o=n("sL3o"),i=n("ziER"),r=n.n(i),s=n("5JeM"),c=n.n(s),l=n("VXtC");const d=new r.a({id:"ctftime",use:"ctftime-usage",viewBox:"0 0 283 80",content:'<symbol xmlns="http://www.w3.org/2000/svg" viewBox="0 0 283 80" id="ctftime"><path fill="#e3000b" d="M0 80h283V0H0l33 40z" /><path fill="#fff" d="M62 58h18v-6H69V28h11v-7H62zm24-30h6v30h7V28h5v-7H86zm24 30h8V43h9v-6h-9v-9h11v-7h-19zm73-33h5v33h5V25h5v-4h-15zm20-4h4v37h-4zm21 14l-5-14h-4v37h4V32l5 13 5-13v26h5V21h-5zm21 19V42h7v-5h-7V25h12l1-4h-18v37h18l-1-4zM136 21v37h39V21zm34 32h-29V26h29v27m-16-14l-6 6 4 4 9-9-16-16h-7z" /></symbol>'});c.a.add(d)}}]);