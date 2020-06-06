<template>
  <section class="page">
    <tweet-layout></tweet-layout>
  </section>
</template>

<script>
import TweetLayout from '~/components/tweet/TweetLayout.vue'

export default {
  components: {
    TweetLayout
  }
}
</script>

<style scoped>
.page {
  margin: 100px;
}
</style>
