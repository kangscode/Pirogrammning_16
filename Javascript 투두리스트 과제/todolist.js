function newRegister() {

    let table = document.getElementById("info");

    let newRow = table.insertRow();

    let newCell1 = newRow.insertCell(0);
    let newCell2 = newRow.insertCell(1);

    newCell1.innerHTML = "<input type='checkbox'>";

    let subject = document.querySelector("#subject");
    let newText = document.createTextNode(subject.value);
    newCell2.innerText = subject.value;

    subject.value = "";

    
}

function delete_Row(rownum) {

    let table = document.getElementById('info');

    if(table.rows.length == 1) {
        return;
    }

    table.deleteRow(rownum);
  }

function btnDelete() {
    let table = document.getElementById('info');
    let num = table.rows.length;

    for(let i=1; i < num; i++) {
        if(document.getElementsByTagName("tr")[i].cells[0].firstChild.checked) {
            table.deleteRow(i);
            num--;
            i--;
        }
    }

}

function deleteAll() {
    let table = document.getElementById('info');
    let num = table.rows.length;

    for(let i=1; i < num; i++) { 
        table.deleteRow(1); 
    }


}