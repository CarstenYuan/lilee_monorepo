<template>
  <div>
    <v-container class="fill-height">
      <v-responsive class="align-centerfill-height">
        <v-data-table
          :headers="headers"
          :items="groups"
          :sort-by="[{ key: 'createdTime', order: 'desc' }]"
        >
          <template v-slot:top>
            <v-toolbar flat>
              <v-toolbar-title>Group List</v-toolbar-title>
              <v-divider class="mx-4" inset vertical></v-divider>
              <v-spacer></v-spacer>
              <v-dialog v-model="dialog" max-width="500px">
                <template v-slot:activator="{ props }">
                  <v-btn class="mb-2" color="primary" dark v-bind="props">
                    Add Group
                  </v-btn>
                </template>
                <v-card>
                  <v-card-title>
                    <span class="text-h5">{{ formTitle }}</span>
                  </v-card-title>

                  <v-card-text>
                    <v-container>
                      <v-row>
                        <v-col cols="12">
                          <v-text-field
                            v-model="editedItem.name"
                            label="Group name"
                          ></v-text-field>
                        </v-col>
                        <v-col cols="12" v-if="editedIndex !== -1">
                          <v-checkbox
                            v-model="editedItem.is_activate"
                            label="Active"
                          ></v-checkbox>
                        </v-col>
                      </v-row>
                    </v-container>
                  </v-card-text>

                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue-darken-1" variant="text" @click="close">
                      Cancel
                    </v-btn>
                    <v-btn color="blue-darken-1" variant="text" @click="save">
                      Save
                    </v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>
              <v-dialog v-model="dialogDelete" max-width="500px">
                <v-card>
                  <v-card-title class="text-h5"
                    >Are you sure you want to delete this item?</v-card-title
                  >
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn
                      color="blue-darken-1"
                      variant="text"
                      @click="closeDelete"
                      >Cancel</v-btn
                    >
                    <v-btn
                      color="blue-darken-1"
                      variant="text"
                      @click="deleteItemConfirm"
                      >OK</v-btn
                    >
                    <v-spacer></v-spacer>
                  </v-card-actions>
                </v-card>
              </v-dialog>
            </v-toolbar>
          </template>
          <template v-slot:item.actions="{ item }">
            <v-icon class="me-2" size="small" @click="editItem(item)">
              mdi-pencil
            </v-icon>
            <v-icon size="small" @click="deleteItem(item)"> mdi-delete </v-icon>
          </template>
        </v-data-table>
      </v-responsive>
    </v-container>

    <v-dialog v-model="errorDialog" width="auto">
      <v-card max-width="400" :text="errorMessage" title="Error">
        <template v-slot:actions>
          <v-btn class="ms-auto" text="Ok" @click="errorDialog = false"></v-btn>
        </template>
      </v-card>
    </v-dialog>
  </div>
</template>

<script setup>
import { ref, computed, nextTick, onMounted } from "vue";
import {
  getAllGroups,
  getSingleGroup,
  addGroup,
  deleteGroup,
  updateGroupInfo,
} from "@/common/api";
import dayjs from "dayjs";

const dialog = ref(false);
const dialogDelete = ref(false);
const headers = [
  {
    title: "Name",
    key: "name",
  },
  { title: "is_Activate", key: "is_activate" },
  { title: "creator", key: "creator" },
  { title: "createdTime", key: "createdTime" },
  { title: "modifier", key: "modifier" },
  { title: "modifiedTime", key: "modifiedTime" },
  { title: "Actions", key: "actions", sortable: false },
];
let groups = ref([]);
let editedIndex = ref(-1);
let editedItem = ref({
  id: -1,
  name: "",
  is_activate: false,
});
let defaultItem = ref({
  id: -1,
  name: "",
  is_activate: false,
});
let errorDialog = ref(false);
let errorMessage = ref("");

const formTitle = computed(() => {
  return editedIndex.value === -1 ? "New Group" : "Edit Group";
});

const editItem = async (item) => {
  try {
    editedIndex.value = groups.value.indexOf(item);
    const user = (await getSingleGroup(item.id)).data;
    editedItem.value = user;
    dialog.value = true;
  } catch (error) {
    errorMessage.value = error.response.data.detail;
    errorDialog.value = true;
  }
};

const deleteItem = (item) => {
  editedIndex.value = groups.value.indexOf(item);
  editedItem.value = Object.assign({}, item);
  dialogDelete.value = true;
};

const deleteItemConfirm = async () => {
  deleteGroup(editedItem.value.id)
    .then(async (response) => {
      console.log(response);
      if (response.status === 200) {
        console.log("delete group success");
        getAllGroupsFromAPI();
      }
      closeDelete();
    })
    .catch((error) => {
      errorMessage.value = error.response.data.detail;
      errorDialog.value = true;
    });
};

const close = () => {
  dialog.value = false;
  nextTick(() => {
    editedItem.value = Object.assign({}, defaultItem);
    editedIndex.value = -1;
  });
};

const closeDelete = () => {
  dialogDelete.value = false;
  nextTick(() => {
    editedItem.value = Object.assign({}, defaultItem);
    editedIndex.value = -1;
  });
};

const save = async () => {
  try {
    if (editedIndex.value > -1) {
      const updateResponse = await updateGroupInfo(editedItem.value.id, {
        name: editedItem.value.name,
        is_activate: editedItem.value.is_activate,
      });
      if (updateResponse.status === 200) {
        console.log("update user success");
      }
    } else {
      const addResponse = await addGroup({
        name: editedItem.value.name,
      });
      if (addResponse.status === 200) {
        console.log("add user success");
      }
    }
    getAllGroupsFromAPI();
    close();
  } catch (error) {
    console.log(error);
    errorMessage.value = error.response.data.detail;
    errorDialog.value = true;
  }
};

const formatData = (data) => {
  const result = data.map((item) => ({
    ...item,
    createdTime: item.createdTime
      ? dayjs(item.createdTime).format("YYYY/MM/DD HH:mm:ss")
      : "-",
    modifiedTime: item.modifiedTime
      ? dayjs(item.modifiedTime).format("YYYY/MM/DD HH:mm:ss")
      : "-",
  }));
  return result;
};

const getAllGroupsFromAPI = () => {
  getAllGroups()
    .then((response) => {
      groups.value = formatData(response.data);
    })
    .catch((error) => {
      errorMessage.value = error.response.data.detail;
      errorDialog.value = true;
    });
};

onMounted(() => {
  getAllGroupsFromAPI();
});
</script>
