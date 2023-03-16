<template>
    <div class="calendar-container">
      <div class="calendar-nav-btns">
        <button @click="previousWeek">Previous</button>
        <button @click="advanceWeek">Next</button>
      </div>
      <div class="calendar-book-btns">
        <button @click="book">Book Sunday</button>
        <button @click="book">Book Monday</button>
        <button @click="book">Book Tuesday</button>
        <button @click="book">Book Wednesday</button>
        <button @click="book">Book Thursday</button>
        <button @click="book">Book Friday</button>
        <button @click="book">Book Saturday</button>
  
      </div>
      <DayPilotCalendar id="dp" :config="config" ref="calendar"/>
    </div>
  </template>
  
  <script>
  import { DayPilot,DayPilotCalendar } from '@daypilot/daypilot-lite-vue'
  import axios from 'axios'
  import PopOut from './PopOut.vue'
  export default {
    name: 'Calendar',
    data: function () {
      return {
        config: {
          viewType: "Week",
          eventResizeHandling: "Disabled",
          eventMoveHandling: "Disabled",
          timeRangeSelectedHandling: "Disabled"
        },
        roomID: -1
      }
    },
    components: {
      DayPilotCalendar,
      PopOut
    },
    computed: {
      calendar() {
        return this.$refs.calendar.control;
      }
    },
    methods: {
      /**
       * loads avlability for the room, this is done by making a request
       * to the backend
       */
      async loadEvents() {
        await this.getRoomId();
        let events = []
        // getting variables needed for get request
        let authToken = window.sessionStorage.getItem('auth');
        let baseUrl = window.location.href;
        let index = baseUrl.indexOf('/', 10);
        baseUrl = baseUrl.slice(0, index);
        // get request for room avlability
        await axios.get(`${baseUrl}/api/testingRoomsAvailability/roomAvailability/`, {
          headers: { 'Authorization': `token ${authToken}` },
          params: {
            id: this.roomID,
          }
        })
          .then((res) => {
            let availability = res.data
            // populating events
            for (let i = 0; i < availability.length; i += 1) {
              let eventText;
              let eventBarColor;
              let startTime = `${availability[i].date}T${availability[i].start_time}`
              let endTime = `${availability[i].date}T${availability[i].end_time}`
              // determining the inner text and bar color
              if (availability[i].is_booked) {
                eventText = "Booked";
                eventBarColor = "red";
              }
              else {
                eventText = "Available";
                eventBarColor = "green";
              }
              // event to be added to events
              let event = {
                id: availability[i].id,
                start: startTime,
                end: endTime,
                text: eventText,
                barColor: eventBarColor
              }
              events.push(event);
            }
          })
          .catch((err) => {
            console.log(err);
          })
  
        this.calendar.update({ events });
      },
      /**
       * getting room id from backend
       */
      async getRoomId() {
        // getting variables needed for get request
        let authToken = window.sessionStorage.getItem('auth');
        let baseUrl = window.location.href;
        let index = baseUrl.indexOf('/', 10);
        baseUrl = baseUrl.slice(0, index);
        // request to get testing room data
        await axios.get(`${baseUrl}/api/testingRooms/getTestingRoom/`, {
          headers: { 'Authorization': `token ${authToken}` },
          params: {
            roomNum: this.$route.params.room,
            bldg: this.$route.params.bldg
          }
        })
          .then(res => {
            this.roomID = res.data[0].id;
          })
          .catch((err) => {
            console.log(err);
          })
      },
      /**
       * Advance the week in dayplot calendar
       */
      advanceWeek() {
        this.calendar.startDate = this.calendar.startDate.addDays(7);
        this.calendar.update();
      },
      /**
       * will go back to previous week in dayplot calendar
       */
      previousWeek() {
        this.calendar.startDate = this.calendar.startDate.addDays(-7);
        this.calendar.update();
      },
      /**
       * toggleing our add availability popout
       */
      togglePopout() {
        if (this.popOutToggle) {
          this.popOutToggle = false;
        }
        else {
          this.popOutToggle = true;
        }
      },
      book() {
        console.log("BOOKED");
      }
    },
    mounted() {
      this.loadEvents();
    }
  }
  </script>
  