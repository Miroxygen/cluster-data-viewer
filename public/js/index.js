/**
 * @file Defines front end configurations.
 * @module public/js/index
 * @author Miranda Holmlund
 * @version 1.0
 */

//Buttons to open and close clusters.
const buttons = document.getElementsByClassName('drop_down')

//Clusters.
const divs = document.getElementsByClassName('data_box')

//Sets an eventlistener for each button to open and close respective cluster.
for (var i = 0; i < buttons.length; i++) {
  buttons[i].addEventListener("click", (event) => {
    const index = event.target.getAttribute('data_index')
    const targetDiv = document.getElementById(`div_${index}`)
    console.log(targetDiv)
    targetDiv.classList.toggle('hidden')
  })
}