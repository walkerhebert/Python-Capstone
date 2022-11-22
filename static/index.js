let btn = document.getElementById('btn');
let output = document.getElementById('output');

let codes = ["WINTER20", "WAKA10", "BRADYISNOTCOOL1", "BRADYISCOOL10", "CODYISMEH", "No code, sorry", "No code, sorry", "No code, sorry", "No code, sorry", "No code, sorry", "No code, sorry", "No code, sorry", "No code, sorry", "No code, sorry", "No code, sorry", "No code, sorry", "No code, sorry", "I hope this makes you smile Cody"];

btn.addEventListener('click', function() {
  let randomCode = codes[Math.floor(Math.random() * codes.length)]
  output.innerHTML = randomCode;
});
