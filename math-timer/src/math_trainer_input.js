interface FormElements {
    solution: HTMLInputElement;
}

const form = document
    .getElementById('math_trainer_form') as HTMLFormElement;
const solution_form = document
    .getElementById('solution_form') as HTMLDivElement;

const elements: FormElements = {
    solution: document
        .getElementById('solution') as HTMLInputElement
};

form
    .addEventListener('submit', (event) => {
        event
            .preventDefault();


        const solutionValue = elements
            .solution.value.trim();

        solution_form.innerHTML = solutionValue;
    });
