import React, {useState} from "react";

export default function TaskForm({ onCreate }) {
    const [title, setTitle] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();
        if (title.trim()) {
            onCreate({ title, completed: false });
            setTitle("");
        }
    };

    return (
        <form onSubmit={handleSubmit} className="mb-4">
            <input
                type="text"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                placeholder="Add a new task"
                className="border p-2 w-64 mr-2 rounded"
            />
            <button type="submit" className="bg-blue-500 text-white p-2 rounded">
                Add Task
            </button>
        </form>
    );
}