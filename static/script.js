document.addEventListener('DOMContentLoaded', function () {
    const calendarEl = document.getElementById('calendar');

    // Assign colors based on priority & completion
    const formattedEvents = taskEvents.map((task, index) => {
        let color = '';

        if (task.done) {
            color = 'gray'; // completed
        } else {
            switch (task.priority.toLowerCase()) {
                case 'high':
                    color = 'red';
                    break;
                case 'medium':
                    color = 'orange';
                    break;
                case 'low':
                    color = 'green';
                    break;
                default:
                    color = 'blue';
            }
        }

        return {
            title: task.task,
            start: task.deadline,
            color: color
        };
    });

    const calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        events: formattedEvents
    });

    calendar.render();
});





// document.addEventListener('DOMContentLoaded', function () {
//     const calendarEl = document.getElementById('calendar');

//     const formattedEvents = taskEvents.map(task => ({
//         title: task.task,
//         start: task.deadline
//     }));

//     const calendar = new FullCalendar.Calendar(calendarEl, {
//         initialView: 'dayGridMonth',
//         events: formattedEvents
//     });

//     calendar.render();
// });
