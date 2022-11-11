editButtons = document.querySelectorAll('.edit-item-quantity');

for (const button of editButtons) {
  button.addEventListener('click', () => {
    const newAmount = prompt('Choose your quantity.');
    const formInputs = {
      updated_amount: newAmount,
      rating_id: button.id,
    };

    fetch('/update_quantity', {
      method: 'POST',
      body: JSON.stringify(formInputs),
      headers: {
        'Content-Type': 'application/json',
      },
    }).then((response) => {
      if (response.ok) {
        document.querySelector(`span.quantity_num_${button.id}`).innerHTML = newAmount;
      } else {
        alert('Failed to update quantity.');
      }
    });
  });
}