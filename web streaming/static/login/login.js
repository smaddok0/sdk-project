const data_daftar = document.querySelector('#data_daftar')
const input_daftar = document.querySelector('.input_daftar')


data_daftar.addEventListener('keydown',function(i){
    if(i.key === 'Enter'){
        i.preventDefault()
        console.log('tidak terjadi apa apa')}
})

data_daftar.addEventListener('input',function(i){
    console.log('data terkirim')
})