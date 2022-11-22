let btn = document.getElementById('btn');
let output = document.getElementById('output');

let quotes = ["WINTER20", "WAKA10", "BRADYISNOTCOOL1", "BRADYISCOOL10", "CODYISMEH", "No code, sorry", "No code, sorry", "No code, sorry", "No code, sorry", "No code, sorry", "No code, sorry", "No code, sorry", "No code, sorry", "No code, sorry", "No code, sorry", "No code, sorry", "No code, sorry", "I hope this makes you smile Cody"];

btn.addEventListener('click', function() {
  let randomQuote = quotes[Math.floor(Math.random() * quotes.length)]
  output.innerHTML = randomQuote;
});
