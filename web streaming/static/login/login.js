const nama = document.querySelector('#nama')
const pass = document.querySelector('#password')
const submit = document.querySelector('#submit')

nama.addEventListener("keydown", function(i){
    if(i.key === 'Enter'){
        i.preventDefault()
        console.log('not submitted')}
})

pass.addEventListener("keydown", function(i){
    if(i.key === 'Enter'){
        i.preventDefault()
        console.log('not submitted')}
})

submit.addEventListener("click",() => {
    fetch("/user/login/submit",{
        method: 'POST',
        headers:{'Content-type':'application/json'},
        body: JSON.stringify({user:nama.value, password:pass.value})    
    })
    .then(res => res.json())
    .then(hasil)
})
function hasil(hasil){
    if (hasil['ada']){
        console.log(hasil['ada'])
        window.location.href = '/'
    }
    else if(hasil['salah']){
        alert(hasil['salah'])
    }
    else{
        alert(hasil['belum'])
    }
}