import baseAPI from "./api";

export const CalculatorAPI = {
  makeCalculations: async (data) => {
    const response = await baseAPI.request({
      url: `calculator/v1/calculate/`,
      method: "POST",
      data: { tokens: Object.values(data) },
    });
    return response.data;
  },
};
