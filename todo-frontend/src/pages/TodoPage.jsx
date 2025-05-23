import React, {useEffect, useState} from "react";
import { getTasks, createTask, updateTask, deleteTask } from "../api/tasks";
import TaskItem from "../components/TaskItem";
import TaskForm from "../components/TaskForm";

export default function TodoPage() {
    const [tasks, setTasks] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        async function fetchTasks() {
            try {
                setLoading(true);
                const data = await getTasks();
                setTasks(data);
            } catch (err) {
                setError("error fetching tasks");
            } finally {
                setLoading(false);
            }
        }
        fetchTasks();
    }, []);

    const handleCreate = async (task) => {
        try {
            const newTask = await createTask(task);
            setTasks(prev => [...prev, newTask]);
        }
        catch (err) {
            alert("error creating task");
        }
    };

    const handleUpdate = async (id, updates) => {
        try {
            const updatedTask = await updateTask(id, updates);
            setTasks(prev => prev.map(task => (task.id === id ? updatedTask : task)));
        } 
        catch (err) {
            alert("error updating task");
        }
    };

    const handleDelete = async (id) => {
        try{
            await deleteTask(id);
            setTasks(prev => prev.filter(task => task.id !== id));
        }
        catch (err) {
            alert("error deleting task");
        }
    };

    if (loading) {
        return <div className="text-center mt-10">Loading...</div>;
    }
    if (error) {
        return <div className="text-center mt-10 text-red-600">{error}</div>;
    }

    return (
        <div className="max-w-md mx-auto mt-10">
            <h1 className="text-2xl font-bold mb-4">Todo List</h1>
            <TaskForm onCreate={handleCreate} />
            {tasks.length === 0 && (
                <div className="text-center mt-4 text-gray-600">No tasks available</div>
            )}
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