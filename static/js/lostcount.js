document.addEventListener('DOMContentLoaded', function() {
    fetch('/lostcount')
        .then(response => response.json())
        .then(data => {
            const userList = document.getElementById('user-list');

            for (const category in data) {
                if (data.hasOwnProperty(category)) {
                    const users = data[category];
                    const categoryHeader = document.createElement('h2');
                    categoryHeader.textContent = category;
                    userList.appendChild(categoryHeader);

                    const userUl = document.createElement('ul');
                    users.forEach(user => {
                        const userLi = document.createElement('li');
                        userLi.textContent = user;
                        userUl.appendChild(userLi);
                    });
                    userList.appendChild(userUl);
                }
            }
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
});