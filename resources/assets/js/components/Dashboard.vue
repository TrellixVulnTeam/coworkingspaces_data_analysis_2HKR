<template>
    <v-container id="dashboard" fluid   grid-list-lg class="mx-0 pa-0">
        <v-layout  row wrap>
            <v-flex md3 sm6 xs12 v-for="(stat, key) in stats.monthlyStats" :key="key">
                <v-card :class="stat.bgColor"   light>
                    <v-container fluid grid-list-sm light>
                        <v-layout class="mt-0 mb-0" row wrap>
                            <v-flex d-flex xs3>
                                <v-icon class="mx-0" x-large light>{{stat.icon}}</v-icon>
                            </v-flex>
                            <v-flex d-flex xs9 >
                                <v-layout class="mt-2 mb-0 pa-0" row wrap>
                                    <v-flex d-flex xs12>

                                        <div class="silver--text subheading">{{stat.title}}</div>

                                    </v-flex>

                                   <v-flex d-flex xs12>
                                         <div class="silver--text display-1">{{stat.data}}</div>
                                       <v-btn outline class="darkgrey--text darken-1" right flat small>{{stat.action.label}}</v-btn>
                                  </v-flex>
                                </v-layout>
                            </v-flex>

                        </v-layout>
                    </v-container>
                </v-card>
            </v-flex>
            </v-layout>
            <v-layout class="pt-1" row wrap>
                <v-flex md4 xs12>
                    <v-card light>
                        <doughnut></doughnut>
                    </v-card>
                </v-flex>
                <v-flex md7 xs12>
                    <v-card light>
                        <bar></bar>
                    </v-card>
                </v-flex>
                <v-flex md11 xs12>
                    <v-card light class="Chart">
                        <line-chart></line-chart>
                    </v-card>
                  </v-flex>

            </v-layout>
    </v-container>
</template>
<script>
import Bar from "../components/chart/Bar";
import Doughnut from "../components/chart/Doughnut";
import LineChart from "../components/chart/LineChart";
export default {
  name: "Dashboard",

  data () {
    return {
      stats: {
        monthlyStats: [
          {
            bgColor: "cyan darken-3",
            icon: "card_membership",
            title: "Followers",
            data: "3439",
            action: {
              label: "More Info",
              link: ""
            }
          },
          {
            bgColor: "deep-orange  lighten-3",
            icon: "card_membership",
            title: "Followers not followed back",
            data: "2747",
            action: {
              label: "More Info",
              link: ""
            }
          },
          {
            bgColor: "blue-grey darken-1",
            icon: "card_membership",
            title: "following",
            data: "2390",
            action: {
              label: "More Info",
              link: ""
            }
          },
          {
            bgColor: "pink  lighten-4",
            icon: "card_membership",
            title: "Mutual friends",
            data: "692",
            action: {
              label: "More Info",
              link: ""
            }
          }
        ]
      }
    };
  },
  components: {
    Bar,
    Doughnut,
    LineChart
  },
  mounted () {}
};
</script>
<style  scoped>
#dashboard .flex {
  margin-bottom: 2px;
}
</style>
