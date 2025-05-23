import React, {useEffect, useState} from "react";
import { getTasks, createTask, updateTask, deleteTask } from "../api/tasks";
import TaskItem from "../components/TaskItem";
import TaskForm from "../components/TaskForm";

export default function TodoPage() {
    const [tasks, setTasks] = useState([]);

    useEffect(() => {
        getTasks().then(setTasks);
    }, []);

    const handleCreate = async (task) => {
        const newTask = await createTask(task);
        setTasks([...tasks, newTask]);
    };

    const handleUpdate = async (id, updates) => {
        const updatedTask = await updateTask(id, updates);
        setTasks(tasks.map(task => (task.id === id ? updatedTask : task)));
    };

    const handleDelete = async (id) => {
        await deleteTask(id);
        setTasks(tasks.filter(task => task.id !== id));
    };

    return (
        <div className="max-w-md mx-auto mt-10">
            <h1 className="text-2xl font-bold mb-4">Todo List</h1>
            <TaskForm onCreate={handleCreate} />
            {tasks.map(task => (
                <TaskItem 
                    key={task.id} 
                    task={task} 
                    onDelete={handleDelete} 
                    onUpdate={handleUpdate} 
                />
            ))}
        </div>
    );
}