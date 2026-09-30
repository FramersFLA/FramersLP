const fs = require('fs');
const vm = require('vm');
const assert = require('assert/strict');
for (const valid of [false, true]) {
 const button = {disabled:true}, status = {}, form = {
   querySelector: (s) => s.includes('button') ? button : status,
   addEventListener: (_,fn) => form.submit = fn,
   reportValidity: () => valid
 };
 const values = {name:'A & B',email:'test@example.com',subject:'Question & clarity?',message:'Line one\nMeaning: # % & ?'};
 const window = {location:{href:''}};
 const context={document:{querySelectorAll:()=>[form]},window,FormData:class {get(k){return values[k]}},encodeURIComponent};
 vm.runInNewContext(fs.readFileSync('docs/site.js','utf8'),context);
 assert.equal(button.disabled,false);
 let prevented=false;form.submit({preventDefault:()=>prevented=true});assert(prevented);
 if(!valid) {assert.equal(window.location.href,'');continue;}
 const url=new URL(window.location.href);
 assert.equal(url.pathname,'foundersfla@gmail.com');
 assert.equal(url.searchParams.get('subject'),values.subject);
 assert.equal(url.searchParams.get('body'),`Name: ${values.name}\nReply email: ${values.email}\n\n${values.message}`);
 assert.match(status.textContent,/Review and send/);
}
console.log('PASS: invalid forms do not open drafts; valid forms encode names, subject, message and newlines; no send-success claim.');
