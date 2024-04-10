import axios from "axios";

export const instance = axios.create({
  baseURL: "http://127.0.0.1:9000/",
});

//Users API
export const getAllUsers = () => instance.get("/getAllUsers");
export const getSingleUser = (id) => instance.get(`/getSingleUser/${id}`);
export const addUser = (data) => instance.post("/addUser", data);
export const updateUserInfo = (id, data) =>
  instance.put(`/updateUserInfo/${id}`, data);
export const deleteUser = (id) => instance.delete(`/deleteUser/${id}`);

//Groups API
export const getAllGroups = () => instance.get("/getAllGroups");
export const getActiveGroups = () => instance.get("/getActiveGroups");
export const getSingleGroup = (id) => instance.get(`/getSingleGroup/${id}`);
export const addGroup = (data) => instance.post("/addGroup", data);
export const updateGroupInfo = (id, data) =>
  instance.put(`/updateGroupInfo/${id}`, data);
export const deleteGroup = (id) => instance.delete(`/deleteGroup/${id}`);
