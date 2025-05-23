import React from "react";

export default function TaskItem({ task, onDelete, onUpdate }) {
    return (
        <div className="flex justify-between items-center border p-2 mb-2 rounded">
            <div>
                <input 
                    type="checkbox"
                    checked={task.completed}
                    onChange={() => onUpdate(task.id, { completed: !task.completed })}
                />
                <span className={`ml-2 ${task.completed ? 'line-through text-gray-500' : ''}`}>
                    {task.title}
                </span>
            </div>
            <button onClick={() => onDelete(task.id)} className="text-red-500">Delete</button>
        </div>    
    )
}