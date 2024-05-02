
////////////////////////////////////////////////////////////////////////////////////
//
// Fill a table's TBODY with rows; the TBODY will be cleared before
// being built
//
////////////////////////////////////////////////////////////////////////////////////


function immo_fillTable(tableID, jsonData) {
    
    // Get the table's TBODY element
    let container = document.getElementById(tableID).getElementsByTagName("tbody");
   
    // Loop through the JSON data and create table rows
  
    let button = null;
  
    jsonData.forEach((item) => {
      let tr = document.createElement("tr");
      
      // Get the values of the current object in the JSON data
      let vals = Object.values(item);
      
      // Loop through the values and create table cells

      vals.forEach((elem, index, arr) => {

        let td = document.createElement("td");

        switch (index) {

          case 0:

            break;  // ignore (don't show) building id

          case 1:

            anchor = document.createElement("a");
            anchor.href = "#";
            anchor.onclick = getBuilding;
            anchor.setAttribute("data-building_id", arr[0]);
            anchor.innerText = elem;
            td.appendChild(anchor);

            break;

          default:

            td.innerText = elem; // Set the value as the text of the table cell
            break;

        }

        tr.appendChild(td); // Append the table cell to the table row
        
      });
      // update button
      td = document.createElement("td");
      button = document.createElement("input"); button.type = "button"; button.value = "update"
      td.appendChild(button);
      tr.appendChild(td); // Append the table cell to the table row
      // delete button
      td = document.createElement("td");
      button = document.createElement("input"); button.type = "button"; button.value = "delete"
      td.appendChild(button);
      tr.appendChild(td); // Append the table cell to the table row
  
      table.appendChild(tr); // Append the table row to the table
    });
    
    container.appendChild(table) // Append the table to the container element
  }
