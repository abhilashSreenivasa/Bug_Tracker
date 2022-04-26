function setId(id) {
  localStorage.setItem("id", id);
}
function setFormAction() {
  const id = localStorage.getItem("id");
  document.getElementById("deleteForm").action = "";
  document.getElementById("deleteForm").action = "delete/" + id;
  return true;
}

function totalBudget() {
  let rows = document.getElementsByName("budgetRow");
  let projected = 0;
  let actual = 0;
  for (let i = 0; i < rows.length; i++) {
    projected = projected + parseInt(rows[i].children[2].innerText);
    actual = actual + parseInt(rows[i].children[3].innerText);
  }
  return actual - projected;
}

window.onload = function () {
  let total = document.getElementById("total");
  if (total) {
    if (totalBudget() >= 0) {
      total.style = "color: dark blue; size: 10vh;";
    } else {
      total.style = "color: dark red; size: 10vh;";
    }
    if (totalBudget() == 0) {
      total.innerText =
        "No surplus and Defecit";
    } else {
      total.innerText = `projected budget ${
        totalBudget() > 0 ? "surplus $" : "deficit $"
      } ${totalBudget()}`;
    }
  }
};
