document.querySelector("button").addEventListener("click", (e)=>{
    e.preventDefault()

    const firstMonth = document.querySelector("#first-month").value
    const secondMonth = document.querySelector("#second-month").value

    const firstMonthValue = document.querySelector(".first-month-value")
    const secondMonthValue = document.querySelector(".second-month-value")

    firstMonthValue.innerHTML = firstMonth
    
    secondMonthValue.innerHTML = secondMonth
})
