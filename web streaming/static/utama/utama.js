
let h1 = 0
let h2 = 0
let h3 = 0
function btn_1() {
    h1 += 1
    document.getElementById("h1").innerText = h1
    // if(h1 == 10){
    //     alert('udah oiiiiii')
    // }
}
function btn_2() {
    h2 += 1
    document.getElementById("h2").innerText = h2
    // if(h2 == 10){
    //     alert('udah oiiiiii')
    // }
}
function btn_3() {
    h3 += 1
    document.getElementById("h3").innerText = h3
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
