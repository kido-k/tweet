<template>
  <section>
    <h1 class="tweet-title">Twitter 解析</h1>
    <tweet-form></tweet-form>
    <tweet-graph></tweet-graph>
  </section>
</template>

<script>
import TweetForm from './TweetForm.vue'
import TweetGraph from './TweetGraph.vue'

export default {
  components: {
    TweetForm,
    TweetGraph
  },
  data() {
    return {}
  },
  computed: {},
  methods: {}
}
</script>

<style scoped>
.tweet-title {
  color: #1976d2;
  font-family: 'Roboto', sans-serif;
  text-align: center;
  font-weight: bold;
  font-size: 36px;
  margin: 0 0 30px 0;
}
</style>
