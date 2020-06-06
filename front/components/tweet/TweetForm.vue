<template>
  <section class="tweet-form">
    <v-form ref="form" v-model="valid">
      <v-text-field
        v-model="keyword"
        :rules="keywordRules"
        label="キーワード"
        required
      ></v-text-field>

      <v-checkbox
        v-model="useRetweet"
        label="リツイートを対象とするか"
        required
      ></v-checkbox>

      <v-btn
        @click="sendData"
        :disabled="!valid"
        color="primary"
        class="mr-4 tweet-button"
        large
      >
        送信
      </v-btn>
    </v-form>
  </section>
</template>

<script>
export default {
  data() {
    return {
      valid: true,
      keyword: '',
      keywordRules: [v => !!v || 'キーワードを入力してください'],
      useRetweet: false,
      baseURL: 'http://localhost:8000/tweet_analyze'
    }
  },
  computed: {},
  methods: {
    sendData() {
      const config = {
        header: {
          'Content-Type': 'application/json;charset=utf-8',
          'Access-Control-Allow-Origin': '*'
        }
      }
      const param = {
        keyword: this.keyword,
        use_retweet: this.useRetweet
      }
      this.$store.dispatch('tweet/tweetAnalyze', {
        url: this.baseURL,
        config,
        param
      })
    }
  }
}
</script>

<style>
.tweet-form {
  background-color: #fff;
  padding: 100px;
}

.tweet-button {
  margin: 30px 0 0 0;
  border-radius: 8px;
  width: 100%;
  font-weight: bold;
}
</style>
