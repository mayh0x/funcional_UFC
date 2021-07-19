package main;

public class carro {
	private int gas;
	private int gasMax;
	private int pass;
	private int passMax;
	private int km;
	static int cont;
	
	public carro() {  //construtor iniciando com valores padrões. 
		this.gasMax = 100; //caso queira fazer uma sobrecarga de contrutor, apague essa função e utilize a função abaixo (sem os comentarios).
		this.passMax = 2;
		setCont(getCont() + 1);
	}
	
	/*
	 * public carro(int combustivel, int passageiros, int distancia) { //construtor com valores dados na main.
	 * 		this.gas = combustivel;
	 *		this.pass = passageiros;
	 *		this.km = distancia;
	 * 
	 * 		this.gasMax = 100;
	 *		this.passMax = 2;
	 *		setCont(getCont() + 1);
	 * }
	 */
	
	private void setGas(int n1) {
		this.gas = n1;
	}
	
	private void setPass(int n2) {
		this.pass = n2;
	}
	
	private void setKm(int n3) {
		this.km = n3;
	}
	
	private void setCont(int n4) {
		this.cont = n4;
	}
	
	public boolean in() { //embarcar
		if (getPass() < getPassMax()) {
			setPass(getPass() + 1);
			return true;
		}
		else {
			return false;
		}
	}
	
	public boolean out() { //desembarcar
		if (getPass() > 0) {
			setPass(getPass() - 1);
			return true;
		}
		else {
			return false;
		}
	}
	
	public void fuel(int valor) { //abastecer
		if (getGas() < getGasMax()) {
			if(getGas() + valor <= getGasMax()) {
				setGas(getGas() + valor);
				System.out.println("Foi abastecido " + valor + " litros");
			}else {
				valor = getGasMax() - getGas();
				setGas(getGasMax());
				System.out.println("Foi abastecido " + valor + " litros");
			}
		}
	}
	
	public boolean drive(int distancia) { //dirigir
		if ((getPass() > 0) && (getGas() > 0)) {
			if (getGas() < distancia) {
				distancia = getGas();
				System.out.println("Foi percorrido " + distancia + " km");
				setKm(getKm() + getGas());
				setGas(0);
				return true;
			}else {
				setKm(getKm() + distancia);
				setGas(getGas() - distancia);
				System.out.println("Foi percorrido " + distancia + " km");
				return true;
			}
		}else {
			return false;
		}
	}
	
	public int getCont() {
		return cont;
	}
	
	public int getPassMax() {
		return passMax;
	}
	
	public int getGasMax() {
		return gasMax;
	}
	
	public int getPass() {
		return pass;
	}
	
	public int getGas() {
		return gas;
	}
	
	public int getKm() {
		return km;
	}
	
	public String toString() {
		return "Passageiros: " + this.getPass() + "; " +
				"Combustivel: " + this.getGas() + "; " +
				"Distancia Percorrida: " + this.getKm() + ".";
	}
}
