<template>
  <section class="tweet-graph">
    <horizontal-bar-chart-js
      v-if="noun.labels.length > 0"
      :labels="noun.labels"
      :datasets="noun.datasets"
    />
    <horizontal-bar-chart-js
      v-if="verb.labels.length > 0"
      :labels="verb.labels"
      :datasets="verb.datasets"
    />
    <horizontal-bar-chart-js
      v-if="adjective.labels.length > 0"
      :labels="adjective.labels"
      :datasets="adjective.datasets"
    />
    <horizontal-bar-chart-js
      v-if="adverb.labels.length > 0"
      :labels="adverb.labels"
      :datasets="adverb.datasets"
    />
  </section>
</template>

<script>
import HorizontalBarChartJs from '../chart/HorizontalBarChartJs'

export default {
  components: {
    HorizontalBarChartJs
  },
  data() {
    return {
      noun: {
        labels: [],
        datasets: [
          {
            label: '名詞',
            backgroundColor: 'blue',
            borderWidth: 1,
            data: []
          }
        ]
      },
      verb: {
        labels: [],
        datasets: [
          {
            label: '動詞',
            backgroundColor: 'green',
            borderWidth: 1,
            data: []
          }
        ]
      },
      adjective: {
        labels: [],
        datasets: [
          {
            label: '形容詞',
            backgroundColor: 'red',
            borderWidth: 1,
            data: []
          }
        ]
      },
      adverb: {
        labels: [],
        datasets: [
          {
            label: '副詞',
            backgroundColor: 'black',
            borderWidth: 1,
            data: []
          }
        ]
      }
    }
  },
  computed: {
    graphData() {
      return this.$store.state.tweet.data
    }
  },
  watch: {
    graphData(val) {
      if (val.noun.length > 0) {
        val.noun.forEach(content => {
          this.noun.labels.push(content[0])
          this.noun.datasets[0].data.push(content[1])
        })
      }
      if (val.verb.length > 0) {
        val.verb.forEach(content => {
          this.verb.labels.push(content[0])
          this.verb.datasets[0].data.push(content[1])
        })
      }
      if (val.adjective.length > 0) {
        val.adjective.forEach(content => {
          this.adjective.labels.push(content[0])
          this.adjective.datasets[0].data.push(content[1])
        })
      }
      if (val.adverb.length > 0) {
        val.adverb.forEach(content => {
          this.adverb.labels.push(content[0])
          this.adverb.datasets[0].data.push(content[1])
        })
      }
    }
  },
  mounted() {
    const tweetData = localStorage.getItem('tweet')
    if (tweetData) {
      this.$store.commit('tweet/setData', JSON.parse(tweetData))
    }
  },
  methods: {}
}
</script>

<style>
.tweet-graph {
  margin: 50px 0 0 0;
}
</style>
