import axios from "axios";

const api = axios.create({
  baseURL: 'http://localhost:8000',  // сюда адрес твоего бэка
});

export async function getTasks() {
    const response = await axios.get(api);
    return response.data;
}

export async function createTask(task) {
    const response = await axios.post(api, task);
    return response.data;
}

export async function updateTask(id, updates) {
    const response = await axios.put(`${api}/${id}`, updates);
    return response.data;
}

export async function deleteTask(id) {
    await axios.delete(`${api}/${id}`);
}