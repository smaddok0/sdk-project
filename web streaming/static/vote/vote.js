
let h1 = 0
let h2 = 0
let h3 = 0
function btn_1() {
    fetch('/content/vote/add1')
        .then(res => res.json())
        .then(vote1)
}

function vote1(vote){
    document.querySelector("#h_1").innerText = vote
    console.log(vote)
}


function btn_2() {
    h2 += 1
    document.getElementById("h_2").innerText = h2
    // if(h2 == 10){
    //     alert('udah oiiiiii')
    // }
}
function btn_3() {
    h3 += 1
    document.getElementById("h_3").innerText = h3
    // if(h3 == 10){
    //     alert('udah oiiiiii')
    // }
}

function nama_hari(){
    let namahari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu","Minggu"]
    let hari = new Date().getDay()
    let x = namahari[hari-1]
    console.log(`hari ini adalah ${x}`)
}
