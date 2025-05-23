import axios from "axios";

const api = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/v1/tasks/api/v1/tasks',  // сюда адрес твоего бэка
});

export async function getTasks() {
    const response = await api.get('/');
    return response.data;
}

export async function createTask(task) {
    const response = await api.post('/', task);
    return response.data;
}

export async function updateTask(id, updates) {
    const response = await api.put(`/${id}`, updates);
    return response.data;
}

export async function deleteTask(id) {
    await api.delete(`/${id}`);
}