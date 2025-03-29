const startBtn = document.getElementById("startBtn");
const winBtn = document.getElementById("winBtn");
const quinellaBtn = document.getElementById("quinellaBtn");
const trifectaBtn = document.getElementById("trifectaBtn");

function startMessage(){
    console.log("start");
}
startBtn.addEventListener("click", startMessage);

function isHit(probability, callback=()=> 1) {
    let rand = Math.random();
    if(rand <= 0 || rand > probability)
        return 0;
    let odds = Math.floor(10 / rand) / 10;
    odds *= callback();
    if (odds != 0)
        return Math.floor(10 * odds) / 10;
    return 0;
}

const message = (odds)=>{
    if (odds)
        console.log("WIN");
    else
        console.log("LOSE");
}

const probability = 0.5;

winBtn.addEventListener("click", function(){
    let odds=isHit(probability);
    message(odds);
    console.log(odds);});

quinellaBtn.addEventListener("click", ()=>{
    let odds = isHit(probability, ()=>isHit(probability));
    message(odds);
    console.log(odds);});

trifectaBtn.addEventListener("click", ()=>{
    let odds=isHit(probability, ()=>isHit(probability, ()=>isHit(probability)));
    message(odds);
    console.log(odds);
})
