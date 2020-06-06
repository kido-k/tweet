<script>
import { HorizontalBar } from 'vue-chartjs'

export default {
  extends: HorizontalBar,
  props: {
    labels: {
      type: Array,
      default: () => []
    },
    datasets: {
      type: Array,
      default: () => []
    }
  },
  data() {
    return {
      sampleLabels: [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
      ],
      sampleDataSets: [
        {
          label: 'Data',
          backgroundColor: '#f87979',
          borderWidth: 1,
          data: [40, 20, 12, 39, 10, 40, 39, 80, 40, 20, 12, 11]
        }
      ]
    }
  },
  mounted() {
    this.renderChart({
      labels: this.labels,
      datasets: this.datasets
    })
  }
}
</script>

<style scoped></style>
