import React, { useState } from "react";
import styles from "./Calculator.module.css";
import { CalculatorAPI } from "../../services/CalculatorAPI.js";

const formOperations = ["+", "-", "*", "/"];

const initResultData = {
  result: 0,
};

const initFormData = {
  operand1: 0,
  operator: "+",
  operand2: 0,
};

export const Calculator = () => {
  const [formData, setFormData] = useState(initFormData);
  const [errors, setErrors] = useState([]);
  const [resultData, setResultData] = useState(initResultData);

  const handleCalculationSubmit = async (e) => {
    e.preventDefault();
    setErrors([]);
    setResultData(initResultData);

    try {
      const result = await CalculatorAPI.makeCalculations(formData);
      setResultData(result);
    } catch (error) {
      if (
        error?.code === "ERR_BAD_REQUEST" &&
        Object.values(error?.response?.data).length > 0
      ) {
        setErrors(Object.values(error?.response?.data).flat());
      } else {
        setErrors(["Something went wrong, try again later"]);
      }
    }
  };

  return (
    <>
      <form className={styles.form} onSubmit={handleCalculationSubmit}>
        <div className={styles.formContainer}>
          <label>
            <span>First Operator</span>
            <input
              name="operand1"
              id="operand1"
              type="number"
              value={formData.operand1}
              onChange={(e) =>
                setFormData({
                  ...formData,
                  operand1: parseFloat(e.target.value),
                })
              }
            />
          </label>
          <label>
            <span>Operator</span>
            <select
              id="operator"
              value={formData.operator}
              onChange={(e) =>
                setFormData({ ...formData, operator: e.target.value })
              }
            >
              {formOperations.map((el) => (
                <option key={el} value={el}>
                  {el}
                </option>
              ))}
            </select>
          </label>
          <label>
            <span>Second Operand</span>
            <input
              name="operand2"
              id="operand2"
              type="number"
              value={formData.operand2}
              onChange={(e) =>
                setFormData({
                  ...formData,
                  operand2: parseFloat(e.target.value),
                })
              }
            />
          </label>
        </div>
        <button type="submit">Count</button>
        <output name="result" for="operand1 operator operand2">
          {resultData.result}
        </output>
        {errors.length > 0 && (
          <div className={styles.errorsContainer}>
            <h2>Errors</h2>
            <ul>
              {errors.map((err) => (
                <li key={err}>{err}</li>
              ))}
            </ul>
          </div>
        )}
      </form>
    </>
  );
};
