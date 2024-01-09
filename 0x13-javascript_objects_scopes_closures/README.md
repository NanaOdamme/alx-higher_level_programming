# JavaScript - Objects, Scopes and Closures

Welcome to this concise guide that delves into various aspects of JavaScript, showcasing its powerful features and concepts.

## Table of Contents

1. [Why JavaScript programming is amazing](#why-javascript-programming-is-amazing)
2. [How to create an object in JavaScript](#how-to-create-an-object-in-javascript)
3. [What `this` means](#what-this-means)
4. [What `undefined` means](#what-undefined-means)
5. [Why the variable type and scope is important](#why-the-variable-type-and-scope-is-important)
6. [What is a closure](#what-is-a-closure)
7. [What is a prototype](#what-is-a-prototype)
8. [How to inherit an object from another](#how-to-inherit-an-object-from-another)

---

### Why JavaScript programming is amazing

JavaScript has grown from a simple scripting language to one of the most versatile and powerful programming languages. Its widespread adoption, both on the client and server sides, combined with its asynchronous capabilities, make it a preferred choice for many developers.

```javascript
console.log("JavaScript is versatile and powerful!");
```

---

### How to create an object in JavaScript

Objects in JavaScript can be created using the object literal syntax:

```javascript
const person = {
    firstName: "John",
    lastName: "Doe",
    age: 30
};
```

---

### What `this` means

The `this` keyword refers to the object it belongs to. Its value is determined by how a function is called.

```javascript
function sayName() {
    console.log(this.name);
}

const obj = {
    name: "Alice",
    speak: sayName
};

obj.speak();  // Outputs: Alice
```

---

### What `undefined` means

In JavaScript, `undefined` represents a variable that has been declared but has not been assigned a value.

```javascript
let variable;
console.log(variable);  // Outputs: undefined
```

---

### Why the variable type and scope is important

Understanding variable type and scope is crucial for avoiding bugs and writing maintainable code. Variables can be `var`, `let`, or `const`, each with its own scope rules.

```javascript
// Scope Example
{
    let localVar = "I'm local!";
}
// console.log(localVar);  // Error: localVar is not defined
```

---

### What is a closure

A closure is a function bundled together with its lexical environment (the surrounding state). It allows a function to access variables from an outer function even after the outer function has finished executing.

```javascript
function outer() {
    let count = 0;
    return function inner() {
        count++;
        console.log(count);
    };
}

const closureFunc = outer();
closureFunc();  // Outputs: 1
closureFunc();  // Outputs: 2
```

---

### What is a prototype

In JavaScript, objects can have a prototype object. When you try to access a property or method of an object that does not exist on the object itself, JavaScript looks for it in the object's prototype.

```javascript
function Person(name) {
    this.name = name;
}

Person.prototype.greet = function() {
    console.log("Hello, " + this.name);
};

const john = new Person("John");
john.greet();  // Outputs: Hello, John
```

---

### How to inherit an object from another

JavaScript uses prototypal inheritance. Objects can inherit properties and methods from other objects.

```javascript
function Animal(name) {
    this.name = name;
}

Animal.prototype.speak = function() {
    console.log(this.name + " makes a sound.");
};

function Dog(name, breed) {
    Animal.call(this, name);
    this.breed = breed;
}

Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog;

Dog.prototype.bark = function() {
    console.log(this.name + " barks.");
};

const myDog = new Dog("Buddy", "Labrador");
myDog.speak();  // Outputs: Buddy makes a sound.
myDog.bark();   // Outputs: Buddy barks.
```

---
