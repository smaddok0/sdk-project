const komen = document.querySelector('#type')
const kirim = document.querySelector('#kirim')
const base = document.querySelector('#cmd_b')

function command(user,text){
    const box = document.createElement('div')
    box.classList.add('box_cmd')

    const user_cmd = document.createElement('span')
    user_cmd.classList.add('user_cmd')
    user_cmd.innerText = user

    const cmd = document.createElement('p')
    cmd.classList.add('cmd')
    cmd.innerText = text

    box.appendChild(user_cmd)
    box.appendChild(cmd)
    return box
}

kirim.addEventListener('click', () =>{
    fetch('/streaming/komen',{
        method:'POST',
        headers:{'Content-type':'application/json'},
        body: JSON.stringify({komen : komen.value})
    })
    .then(res => res.json())
    .then(hasil)    
    komen.value = ""
})

function hasil(hasil){
    base.appendChild(command('smaddok',hasil))
}


