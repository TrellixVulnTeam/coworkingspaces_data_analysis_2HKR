<template>
  <v-container fluid>
    <v-flex xs12>
      <v-card>
        <v-card-title>
          Members
          <v-spacer></v-spacer>
          <v-btn class="blue-grey" fab small dark @click.native.stop="rightDrawer = !rightDrawer">
            <v-icon>search</v-icon>
          </v-btn>
          &nbsp;
          <v-btn class="purple" fab small @click.native="add">
            <v-icon>add</v-icon>
          </v-btn>
          &nbsp;
          <v-btn class="grey" fab small dark @click.native="print">
            <v-icon>print</v-icon>
          </v-btn>
        </v-card-title>
        <v-data-table 
          class="elevation-1" 
          :headers="headers" 
          :items="items"
          hide-actions>

          <template class="body-2" slot="items" slot-scope="props">            
            <td class="text-xs-left">{{ props.item.firstname }}</td>
            <td class="text-xs-right">{{ props.item.lastname }}</td>
            <td class="text-xs-right">{{ props.item.email }}</td>
            <td class="text-xs-right">{{ props.item.age }}</td>            
            <td class="text-xs-right">
              <v-icon class="light" v-if="props.item.isActive">done</v-icon>
              <v-icon class="light" v-else>block</v-icon>
            </td>
            <td class="text-xs-right">
              <v-btn class="indigo" fab small @click.native="changeStatus(props.item)">
                <v-icon>autorenew</v-icon>
              </v-btn>
              <v-btn class="teal" fab small dark @click.native="edit(props.item)">
                <v-icon>edit</v-icon>
              </v-btn>
              <v-btn class="cyan" fab small @click.native="remove(props.item)">
                <v-icon>delete</v-icon>
              </v-btn>
            </td>
          </template>
        </v-data-table>
        <div class="text-xs-center pt-2">
          <v-pagination v-model="pagination.page" :length="pages" circle></v-pagination>
          <!-- Math.ceil(pagination.totalItemstotalItems / pagination.rowsPerPage) -->
        </div>
      </v-card>
    </v-flex>

    <v-navigation-drawer temporary :right="right" v-model="rightDrawer" fixed>
      <v-list>
        <v-list-tile-title>&nbsp;</v-list-tile-title>
        <v-list-tile>
          <v-list-tile-title>Search Panel</v-list-tile-title>
          <v-list-tile-action>
            <v-btn @click.native="searchCustomers">
              <v-icon dark>search</v-icon>
            </v-btn>
          </v-list-tile-action>
        </v-list-tile>
        <v-list-tile-title>&nbsp;</v-list-tile-title>
        <v-layout row>
          <v-flex xs11 offset-xs1>
            <v-text-field name="input-1-3" label="Frist Name" light v-model="searchVm.contains.firstName"></v-text-field>
          </v-flex>
        </v-layout>
        <v-layout row>
          <v-flex xs11 offset-xs1>
            <v-text-field name="input-1-3" label="Last Name" light v-model="searchVm.contains.lastName"></v-text-field>
          </v-flex>
        </v-layout>
        <v-layout row>
          <v-flex xs11 offset-xs1>
            <v-subheader class="text-sm-central" light>Age range between Age 1 and Age 2 </v-subheader>
          </v-flex>
        </v-layout>
        <v-layout row>
          <v-flex xs8 offset-xs1>
            <v-slider label="Age 1" light v-bind:max="50" v-model="searchVm.between.age.former"></v-slider>
          </v-flex>
          <v-flex xs3>
            <v-text-field type="number" light v-model="searchVm.between.age.former"></v-text-field>
          </v-flex>
        </v-layout>
        <v-layout row>
          <v-flex xs8 offset-xs1>
            <v-slider label="Age 2" light v-bind:max="100" v-model="searchVm.between.age.latter"></v-slider>
          </v-flex>
          <v-flex xs3>
            <v-text-field type="number" light v-model="searchVm.between.age.latter"></v-text-field>
          </v-flex>
        </v-layout>
        <v-list-tile>
          <v-list-tile-title></v-list-tile-title>
          <v-list-tile-action>
            <v-btn @click.native="clearSearchFilters">
              <v-icon dark>clear</v-icon>
            </v-btn>
          </v-list-tile-action>
        </v-list-tile>

      </v-list>
    </v-navigation-drawer>
    <v-snackbar :timeout="2500" :top="true" :error="true" :multi-line="true" v-model="snackbar">
      {{ errText }}
      <v-btn flat light @click.native="snackbar = false">Close</v-btn>
    </v-snackbar>
  </v-container>
</template>


<script>
  export default {
    data () {
      return {
        rightDrawer: false,
        right: true,
        search: '',
        errText: '',
        pagination: {
          page: 1,
          totalItems: 0,
          rowsPerPage: 10
        },
        snackbar: false,
        headers: [
          {
            text: 'First Name',
            left: true,
            sortable: false,
            value: 'firstName'
          },
          { text: 'Last Name', value: 'lastName' },
          { text: 'Email', value: 'email' },
          { text: 'Age', value: 'age' },
          
          { text: 'Active', value: 'isActive' },
          { text: '', value: '' }
        ],
        items: [
          {firstname: 'Salah',lastname: 'Hmidi',email: 'salahhmidi@gmail.com',age: 24,active:'yes'},
          {firstname: 'Fatma',lastname: 'Krir',email: 'fatmakrir@gmail.com',age: 27,active:'yes'},
          {firstname: 'Mariem',lastname: 'Salhi',email: 'mariemsalhi@gmail.com',age: 25,active:'yes'},
          {firstname: 'Ahmed',lastname: 'ouni',email: 'ahmedouni@yahoo.com',age: 28,active:'yes'}
        ],
        searchVm: {
          contains: {
            firstName: '',
            lastName: ''
          },
          between: {
            age: { former: 0, latter: 0 }
          }
        }
      }
    },
    methods: {
      print () {
        window.print()
      },
      edit (item) {
        this.$router.push({ name: 'Customer', params: { id: item.id } })
      },
      add () {
        this.$router.push('/dashboard/newmember')
      },
      remove (item) {
        const rootComponent = this.appUtil.getRootComponent(this)
        if (rootComponent) {
          rootComponent.openDialog('Do you want to delete this customer?', '', () => {
            this.api.deleteData('customers/' + item.id.toString()).then((res) => {
              this.getCustomers()
            }, (err) => {
              console.log(err)
              this.snackbar = true
              this.errText = 'Status has not be deleted successfully. Please try again.'
            })
          })
        }
      },
      changeStatus (item) {
        item.isActive = !item.isActive
        this.api.putData('customers/' + item.id.toString(), item).then((res) => {
          // this.$router.push('Customers')
        }, (err) => {
          console.log(err)
          this.snackbar = true
          this.errText = 'Status has not be updated successfully. Please try again.'
          item.isActive = !item.isActive
        })
      },
      /* searchCustomers () {
        this.rightDrawer = !this.rightDrawer
        this.appUtil.buildSearchFilters(this.searchVm)
        let query = this.appUtil.buildJsonServerQuery(this.searchVm)

        this.api.getData('customers?' + query).then((res) => {

          this.items = res.data
          this.items.forEach((item) => {
            if (item.orders && item.orders.length) {
              item.orderRecord = item.orders.length
            } else {
              item.orderRecord = 0
            }
          })
          this.pagination.totalItems = this.items.length
        }, (err) => {
          console.log(err)
        })
      }, */
     /*  clearSearchFilters () {
        this.rightDrawer = !this.rightDrawer
        this.appUtil.clearSearchFilters(this.searchVm)

        this.api.getData('customers').then((res) => {
          this.items = res.data
          this.items.forEach((item) => {
            if (item.orders && item.orders.length) {
              item.orderRecord = item.orders.length
            } else {
              item.orderRecord = 0
            }
          })
          this.pagination.totalItems = this.items.length
          console.log(this.items)
        }, (err) => {
          console.log(err)
        })
      }, */
     /*  getCustomers () {
        this.api.getData('customers?_embed=orders').then((res) => {
          this.items = res.data
          this.items.forEach((item) => {
            // item.avatar = '/assets/' + item.avatar
            if (item.orders && item.orders.length) {
              item.orderRecord = item.orders.length
            } else {
              item.orderRecord = 0
            }
          })
          this.pagination.totalItems = this.items.length
        }, (err) => {
          console.log(err)
        })
      } */
    },
    computed: {
      pages () {
        return this.pagination && this.pagination.rowsPerPage ? Math.ceil(this.pagination.totalItems / this.pagination.rowsPerPage) : 0
      }
    },
    mounted () {
      //this.getCustomers()
    }
  }
</script>
