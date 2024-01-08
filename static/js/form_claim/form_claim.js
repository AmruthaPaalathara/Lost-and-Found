Vue.use(VueFormWizard)
new Vue({
  el: '#app',
  methods: {
    onComplete: function() {
      alert('Your claim has been successfully submitted');
    }
  }
})

$('input[type="radio"][name="radio1"]').on('change', function() {
    $('textarea[name="textarea"]').toggle($.trim(this.value)=='1');
});
$('input[type="radio"][name="radio2"]').on('change', function() {
    $('textarea[name="textarea2"]').toggle($.trim(this.value)=='1');
});