// initializingdata table//

const dataTable = new simpleDatatables.DataTable("#datatable", {
    searchable: true,
    fixedHeight: true,
    data: [],

});
dataTable.rows.add([
    ["23122001", "watch", "15-11-2023"],
    ["23122001", "watch", "15-11-2023"],
    ["23122001", "watch", "15-11-2023"],
])

fetch("/datatable")
    .then(res => res.json())
    .then(data => {
        dataTable.rows.add(data.data)

    })