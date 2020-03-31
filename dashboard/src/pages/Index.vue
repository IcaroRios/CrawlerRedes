<template>
  <q-page class="flex">
    <div class="q-pa-md full-width">
      <q-table
        title="Congeladores"
        :data="data"
        :columns="columns"
        row-key="name"
        bordered
        table-header-class="bg-blue-3"
        table-bottom-class="bg-blue-3"
      />
    </div>
  </q-page>
</template>
<script>
import Vue from 'vue'
export default {
  name: 'PageIndex',
  mounted () {
    Vue.prototype.$axios.get('http://3.91.0.98/crawlerPythonPDF/teste.txt?_=1585636130510').then(function (response) {
      console.log(response.data)
    })
  },
  data () {
    return {
      columns: [
        { name: 'fornecedor', label: 'Fornecedor', field: 'fornecedor' },
        { name: 'marca', label: 'Marca', field: 'marca' },
        { name: 'modelo', label: 'Modelo', field: 'modelo' },
        { name: 'volume', label: 'Volume', field: 'volume' },
        { name: 'consumo_127', label: 'Consumo 127V', field: 'consumo_127' },
        { name: 'consumo_220', label: 'Consumo 220V', field: 'consumo_220' },
        { name: 'eficiencia_127', label: 'Eficiência 127V', field: 'eficiencia_127' },
        { name: 'eficiencia_220', label: 'Eficiência 220V', field: 'eficiencia_220' },
        { name: 'classificacao_127', label: 'Classificação 127V', field: 'classificacao_127' },
        { name: 'classificacao_220', label: 'Classificação 220V', field: 'classificacao_220' }
      ],
      data: [
        { fornecedor: 'PHILCO', marca: 'PHILCO', modelo: 'CHB42D', volume: 675, consumo_127: 35, consumo_220: 45, eficiencia_127: 0.786, eficiencia_220: 0.746, classificacao_127: 'D', classificacao_220: 'D' },
        { fornecedor: 'PHILCO', marca: 'PHILCO', modelo: 'CHB42D', volume: 675, consumo_127: 35, consumo_220: 45, eficiencia_127: 0.786, eficiencia_220: 0.746, classificacao_127: 'D', classificacao_220: 'D' },
        { fornecedor: 'PHILCO', marca: 'PHILCO', modelo: 'CHB42D', volume: 675, consumo_127: 35, consumo_220: 45, eficiencia_127: 0.786, eficiencia_220: 0.746, classificacao_127: 'D', classificacao_220: 'D' },
        { fornecedor: 'PHILCO', marca: 'PHILCO', modelo: 'CHB42D', volume: 675, consumo_127: 35, consumo_220: 45, eficiencia_127: 0.786, eficiencia_220: 0.746, classificacao_127: 'D', classificacao_220: 'D' },
        { fornecedor: 'PHILCO', marca: 'PHILCO', modelo: 'CHB42D', volume: 675, consumo_127: 35, consumo_220: 45, eficiencia_127: 0.786, eficiencia_220: 0.746, classificacao_127: 'D', classificacao_220: 'D' },
        { fornecedor: 'PHILCO', marca: 'PHILCO', modelo: 'CHB42D', volume: 675, consumo_127: 35, consumo_220: 45, eficiencia_127: 0.786, eficiencia_220: 0.746, classificacao_127: 'D', classificacao_220: 'D' },
        { fornecedor: 'PHILCO', marca: 'PHILCO', modelo: 'CHB42D', volume: 675, consumo_127: 35, consumo_220: 45, eficiencia_127: 0.786, eficiencia_220: 0.746, classificacao_127: 'D', classificacao_220: 'D' },
        { fornecedor: 'PHILCO', marca: 'PHILCO', modelo: 'CHB42D', volume: 675, consumo_127: 35, consumo_220: 45, eficiencia_127: 0.786, eficiencia_220: 0.746, classificacao_127: 'D', classificacao_220: 'D' },
        { fornecedor: 'PHILCO', marca: 'PHILCO', modelo: 'CHB42D', volume: 675, consumo_127: 35, consumo_220: 45, eficiencia_127: 0.786, eficiencia_220: 0.746, classificacao_127: 'D', classificacao_220: 'D' },
        { fornecedor: 'PHILCO', marca: 'PHILCO', modelo: 'CHB42D', volume: 675, consumo_127: 35, consumo_220: 45, eficiencia_127: 0.786, eficiencia_220: 0.746, classificacao_127: 'D', classificacao_220: 'D' },
        { fornecedor: 'PHILCO', marca: 'PHILCO', modelo: 'CHB42D', volume: 675, consumo_127: 35, consumo_220: 45, eficiencia_127: 0.786, eficiencia_220: 0.746, classificacao_127: 'D', classificacao_220: 'D' }
      ]
    }
  }
}
</script>
