
let h1 = 0
let h2 = 0
let h3 = 0
// ----------vote1-------------
document.addEventListener("DOMContentLoaded",function preview1() {
    fetch('/content/vote/preview1')
        .then(res => res.json())
        .then(vote1)
})
function btn_1() {
    fetch('/content/vote/add1')
        .then(res => res.json())
        .then(vote1)
}
function vote1(vote){
    document.querySelector("#h_1").innerText = vote
    console.log(vote)
}


// ----------------vote2----------------------------
document.addEventListener("DOMContentLoaded",function preview2() {
    fetch('/content/vote/preview2')
        .then(res => res.json())
        .then(vote2)
})
function btn_2() {
    fetch('/content/vote/add2')
        .then(res => res.json())
        .then(vote2)
}
function vote2(vote){
    document.querySelector("#h_2").innerText = vote
    console.log(vote)
}


// -----------------------vote3------------------
document.addEventListener("DOMContentLoaded",function preview3() {
    fetch('/content/vote/preview3')
        .then(res => res.json())
        .then(vote3)
})
function btn_3() {
    fetch('/content/vote/add3')
        .then(res => res.json())
        .then(vote3)
}
function vote3(vote){
    document.querySelector("#h_3").innerText = vote
    console.log(vote)
}









// function nama_hari(){
//     let namahari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu","Minggu"]
//     let hari = new Date().getDay()
//     let x = namahari[hari-1]
//     console.log(`hari ini adalah ${x}`)
// }
