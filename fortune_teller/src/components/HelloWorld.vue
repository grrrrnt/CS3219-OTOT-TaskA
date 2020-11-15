<template>
  <div class="hello">
    <h1>Fortune Teller</h1>
    <div>Your lucky number is: {{ lucky_number }}</div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data() {
    return {
      lucky_number: 0
    };
  },
  async mounted() {
    await axios({ method: "GET", "url": "http://localhost/luckynumber" })
      .then(result => {
        this.lucky_number = result.data["lucky_number"];
      }, error => {
        console.error(error);
      })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
