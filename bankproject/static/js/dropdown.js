
        function populateCities() {
            var country = document.getElementById("country").value;
            var cityDropdown = document.getElementById("city");

            cityDropdown.innerHTML = "";

            if (country === "USA") {
                var cities = ["New York", "Los Angeles", "Chicago"];
            } else if (country === "Canada") {
                var cities = ["Toronto", "Vancouver", "Montreal"];
            } else if (country === "UK") {
                var cities = ["London", "Manchester", "Edinburgh"];
            }

            for (var i = 0; i < cities.length; i++) {
                var option = document.createElement("option");
                option.value = cities[i];
                option.text = cities[i];
                cityDropdown.appendChild(option);
            }
        }
