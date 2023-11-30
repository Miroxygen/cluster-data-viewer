

const buttons = document.getElementsByClassName('drop_down')
const divs = document.getElementsByClassName('data_box')

for (var i = 0; i < buttons.length; i++) {
  buttons[i].addEventListener("click", (event) => {
    const index = event.target.getAttribute('data_index')
    const targetDiv = document.getElementById(`div_${index}`)
    console.log(targetDiv)
    targetDiv.classList.toggle('hidden')
  })
}