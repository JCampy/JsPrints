// function for checking check box in account management.html

/*function showConfirmation() {
  const myForm = document.getElementById("customer-info");

  myForm.document.getElementById("cart__button").onsubmit = function (e) {
    e.preventDefault();
    document.getElementById("outer__shopping__cart").style.display = "none";
    document.getElementById("outer__order__confirmation").style.display =
      "flex";
    console.log("form submitted");
  };
} */

function updateBillingCheckBox() {
  var Checkbox = document.getElementById("same-as-shipping");
  var div = document.getElementById("billing-address");

  if (Checkbox.checked) {
    div.style.display = "none";
  } else {
    div.style.display = "contents";
  }
}

var checkbox = document.getElementById("same-as-shipping");
checkbox.addEventListener("change", updateBillingCheckBox);

function updateShippingCheckBox() {
  var Checkbox = document.getElementById("update-shipping");
  var div = document.getElementById("shipping-address");
  var ship_add = document.getElementById("shown_shipping");

  if (Checkbox.checked) {
    div.style.display = "contents";
    ship_add.style.display = "none";
  } else {
    div.style.display = "none";
    ship_add.style.display = "contents";
  }
}

var checkbox = document.getElementById("update-shipping");
checkbox.addEventListener("change", updateShippingCheckBox);

document.addEventListener("DOMContentLoaded", function (event) {
  updateBillingCheckBox();
  updateShippingCheckBox();
});
